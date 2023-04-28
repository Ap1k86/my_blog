from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


# Модель посты.
class Post(models.Model):
    h1 = models.CharField(max_length=200, verbose_name="Заголовок")
    title = models.CharField(max_length=200, verbose_name="Заголовок ")
    url = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField(verbose_name="Описание")
    options = RichTextUploadingField(verbose_name="Параметры содержания")
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    keyword = models.CharField(max_length=200, default='123')
    objects = models.Model

    class Meta:
        verbose_name = 'Пост главной страницы'
        verbose_name_plural = 'Посты на главной странице'

    def __str__(self):
        return self.title


# Модель комментарии.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Model

    class Meta:
        verbose_name = 'Комментарий под постом главной страницы'
        verbose_name_plural = 'Комментарии под постом главной страницы'
        ordering = ['-created_date']

    def __str__(self):
        return self.text


# Модель постов на форуме.
class ForumPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок ")
    content = RichTextUploadingField(verbose_name="Описание")
    img = models.ImageField(upload_to='forum', null=True, blank=True)
    created_at = models.DateField(default=timezone.now)
    author = models.ManyToManyField(User, verbose_name="Автор")
    keyword = models.CharField(max_length=200, default='аквариум, рыбки')
    objects = models.Model

    class Meta:
        verbose_name = 'Пост на форуме'
        verbose_name_plural = 'Посты на форуме'

    def __str__(self):
        return self.title


# Модель комментарии на форуме.
class CommentForum(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments_forum')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_forum')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    objects = models.Model

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии на форуме'
        ordering = ['-created_date']

    def __str__(self):
        return self.text
