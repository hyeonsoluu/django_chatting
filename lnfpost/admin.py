from django.contrib import admin

# Register your models here.
from .models import PostGet_Question

class PostGet_QuestionAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(PostGet_Question, PostGet_QuestionAdmin)