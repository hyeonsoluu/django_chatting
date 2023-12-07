from django import forms
from lnfpost.models import PostGet_Question, PostGet_Answer, PostGet_Comment


class PostGet_QuestionForm(forms.ModelForm):
    class Meta:
        model = PostGet_Question  # 사용할 모델
        fields = ['title', 'category', 'Ddate', 'firstLocation', 'detailLocation', 'storage', 'detailContext']

        labels = {
                    'category': '카테고리',
                    'title': '제목',
                    'Ddate': '분실날짜',
                    'firstLocation': '분실위치',
                    'detailLocation': '상세위치',
                    'storage': '보관장소',
                    'detailContext': '내용',
                }

class PostGet_AnswerForm(forms.ModelForm):
    class Meta:
        model = PostGet_Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class PostGet_CommentForm(forms.ModelForm):
    class Meta:
        model = PostGet_Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }