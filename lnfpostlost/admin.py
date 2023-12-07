from django.contrib import admin

# Register your models here.

from .models import PostLost_Question

class PostLost_QuestionAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(PostLost_Question, PostLost_QuestionAdmin)