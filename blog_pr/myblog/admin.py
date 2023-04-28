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
    pass


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentForum)
class CommentForum(admin.ModelAdmin):
    pass
