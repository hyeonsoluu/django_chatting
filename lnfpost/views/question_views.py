from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import PostGet_Question, PostGet_Answer
from ..forms import PostGet_QuestionForm, PostGet_AnswerForm

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = PostGet_QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('lnfpost:index')
    else:
        form = PostGet_QuestionForm()
    context = {'form': form}
    return render(request, 'lnfpost/post_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(PostGet_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('lnfpost:detail', question_id=question.id)
    if request.method == "POST":
        form = PostGet_QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('lnfpost:detail', question_id=question.id)
    else:
        form = PostGet_QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'lnfpost/post_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(PostGet_Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('lnfpost:detail', question_id=question.id)
    question.delete()
    return redirect('lnfpost:index')

@login_required(login_url='common:login')
def question_vote(request, question_id):
    question = get_object_or_404(PostGet_Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        question.voter.add(request.user)
    return redirect('lnfpost:detail', question_id=question.id)