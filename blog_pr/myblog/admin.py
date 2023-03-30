from django.contrib import admin

# Импортирую модели!
from .models import *


# Зарегистрировал модель POST в админке.
class PostAdmin(admin.ModelAdmin):
    # Для автозаполнения url в админке. Значение берется из title.
    prepopulated_fields = {'url': ('title',)}
    pass

#
# # Зарегистрировал модель Comment в админке.
# class CommentAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, PostAdmin)
