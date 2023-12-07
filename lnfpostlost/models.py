from django.db import models
from django.contrib.auth.models import User

class PostLost_Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postlost_author_question')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    Ddate = models.DateField()
    firstLocation = models.CharField(max_length=200)
    detailLocation = models.CharField(max_length=200)
    detailContext = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='postlost_voter_question')  # 추천인 추가

class PostLost_Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postlost_author_answer')
    question = models.ForeignKey(PostLost_Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='postlost_voter_answer')

class PostLost_Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(PostLost_Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(PostLost_Answer, null=True, blank=True, on_delete=models.CASCADE)