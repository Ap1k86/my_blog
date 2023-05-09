import requests
from django.contrib import admin
from .models import *


# Зарегистрировал модель Post в админке.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Для автозаполнения url в админке. Значение берется из title.
    prepopulated_fields = {'url': ('title',)}
    pass


# Зарегистрировал модель Comment в админке.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'username', 'text', 'created_date')
    fields = ['post', 'username', 'text', 'created_date']
    exclude = ['', ]


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'content', 'created_at', 'author')


@admin.register(CommentForum)
class CommentForum(admin.ModelAdmin):
    list_display = ('post', 'username', 'text', 'created_date')
    exclude = ['', ]


# Почитать на досуге.
# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
