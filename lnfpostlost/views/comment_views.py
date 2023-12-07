from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import PostLost_CommentForm
from ..models import PostLost_Question, PostLost_Answer, PostLost_Comment


@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    """
    pybo 질문댓글등록
    """
    question = get_object_or_404(PostLost_Question, pk=question_id)
    if request.method == "POST":
        form = PostLost_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('lnfpostlost:detail', question_id=question.id)
    else:
        form = PostLost_CommentForm()
    context = {'form': form}
    return render(request, 'lnfpostlost/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    """
    pybo 질문댓글수정
    """
    comment = get_object_or_404(PostLost_Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('lnfpostlost:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = PostLost_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('lnfpostlost:detail', question_id=comment.question.id)
    else:
        form = PostLost_CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'lnfpostlost/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    """
    pybo 질문댓글삭제
    """
    comment = get_object_or_404(PostLost_Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('lnfpostlost:detail', question_id=comment.question_id)
    else:
        comment.delete()
    return redirect('lnfpostlost:detail', question_id=comment.question_id)


@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):
    """
    pybo 답글댓글등록
    """
    answer = get_object_or_404(PostLost_Answer, pk=answer_id)
    if request.method == "POST":
        form = PostLost_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('lnfpostlost:detail', question_id=comment.answer.question.id)
    else:
        form = PostLost_CommentForm()
    context = {'form': form}
    return render(request, 'lnfpostlost/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    pybo 답글댓글수정
    """
    comment = get_object_or_404(PostLost_Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('lnfpostlost:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = PostLost_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('lnfpostlost:detail', question_id=comment.answer.question.id)
    else:
        form = PostLost_CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'lnfpostlost/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    pybo 답글댓글삭제
    """
    comment = get_object_or_404(PostLost_Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('lnfpostlost:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('lnfpostlost:detail', question_id=comment.answer.question.id)