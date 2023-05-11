from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Зарегистрировал модель Post в админке.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Для автозаполнения url в админке. Значение берется из title.
    prepopulated_fields = {'url': ('title',)}
    list_display = ('id', 'title', 'get_photo', 'author', 'created_at')

    # Метод отображения фотографий в админке
    @staticmethod
    def get_photo(obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=150')


# Зарегистрировал модель Comment в админке.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'text', 'username', 'created_date')
    fields = ['post', 'username', 'text', 'created_date']
    # exclude = ['', ]


# Зарегистрировал модель ForumPost в админке.
@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}
    list_display = ('title', 'content', 'get_photo', 'author', 'created_at')

    # Метод отображения фотографий в админке
    @staticmethod
    def get_photo(obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=150')


# Зарегистрировал модель CommentForum в админке.
@admin.register(CommentForum)
class CommentForum(admin.ModelAdmin):
    list_display = ('post', 'text', 'username', 'created_date')
    # exclude = ['created_date', ]


# Почитать на досуге.
# https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
