from django import forms
from lnfpostlost.models import PostLost_Question, PostLost_Answer, PostLost_Comment


class PostLost_QuestionForm(forms.ModelForm):
    class Meta:
        model = PostLost_Question  # 사용할 모델
        fields = ['title', 'category', 'Ddate', 'firstLocation', 'detailLocation', 'detailContext']

        labels = {
            'category': '카테고리',
            'title': '제목',
            'Ddate': '분실날짜',
            'firstLocation': '분실위치',
            'detailLocation': '상세위치',
            'detailContext': '내용',
        }

class PostLost_AnswerForm(forms.ModelForm):
    class Meta:
        model = PostLost_Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class PostLost_CommentForm(forms.ModelForm):
    class Meta:
        model = PostLost_Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }