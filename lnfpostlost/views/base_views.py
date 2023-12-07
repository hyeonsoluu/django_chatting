from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import PostLost_Question, PostLost_Answer
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = PostLost_Question.objects.order_by('create_date')
    if kw:
        question_list = question_list.filter(
            Q(title__icontains=kw) |  # 제목 검색
            Q(category__icontains=kw) |  # 카테고리 검색
            Q(Ddate__icontains=kw) |  # 분실날짜 검색
            Q(firstLocation__icontains=kw) |  # 분실주소 검색
            Q(detailLocation__icontains=kw) |  # 상세주소 검색
            Q(detailContext__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'lnfpostlost/postlost_list.html', context)

def detail(request, question_id):
    question = PostLost_Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'lnfpostlost/postlost_detail.html', context)