from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Для автозаполнения slug. https://pypi.org/project/django-autoslug/
from autoslug import AutoSlugField


# Модель посты.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок:")
    url = models.SlugField(verbose_name='URL-адрес(авто):')
    description = RichTextUploadingField(verbose_name='Описание')
    content = RichTextUploadingField(verbose_name='Подробное описание:')
    options = RichTextUploadingField(verbose_name='Параметры содержания:')
    image = models.ImageField(verbose_name='Фото:')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания:')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.all, verbose_name='Автор:')
    keyword = models.CharField(max_length=200, default='123', verbose_name='Слова для поиска:')
    objects = models.Model

    class Meta:
        verbose_name = 'Пост главной страницы'
        verbose_name_plural = 'Посты на главной странице'

    def __str__(self):
        return self.title


# Модель комментарии.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Текст:')
    username = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя:')
    text = models.TextField(verbose_name='Комментарий:')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания:')
    objects = models.Model

    class Meta:
        verbose_name = 'Комментарий под постом главной страницы'
        verbose_name_plural = 'Комментарии под постом главной страницы'
        ordering = ['-created_date']

    def __str__(self):
        return self.text


# Модель постов на форуме.
class ForumPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок:")
    url = AutoSlugField(unique=True, verbose_name='Заголовок на английском')  # https://pypi.org/project/django-autoslug/
    content = models.TextField(verbose_name="Описание:")
    image = models.ImageField(upload_to='forum', verbose_name='Фото:')
    created_at = models.DateField(default=timezone.now, verbose_name='Дата создания поста:')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор:")
    objects = models.Model

    class Meta:
        verbose_name = 'Пост на форуме'
        verbose_name_plural = 'Посты на форуме'

    # Хз зачем Оно :)
    def __repr__(self):
        return 'ForumPost(%s, %s, %s, %s, %s, %s)' % (
            self.title, self.url, self.content, self.image, self.created_at, self.author)

    def __str__(self):
        return self.title


# Модель комментарии на форуме.
class CommentForum(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments_forum', verbose_name='Текст:')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name_forum', verbose_name='Имя:')
    text = models.TextField(verbose_name='Комментарий:')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания:')
    objects = models.Model

    class Meta:
        verbose_name = 'Комментарий под постом на форуме'
        verbose_name_plural = 'Комментарии на форуме'
        ordering = ['-created_date']

    def __str__(self):
        return self.text
