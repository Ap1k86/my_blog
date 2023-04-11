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
        ordering = ['-created_date']

    def __str__(self):
        return self.text


# Модель для хранения фоток в слайдере.(Карусель). ДУМАЙ.
class Visual(models.Model):
    class Meta:
        db_table = 'app_ideator_visuals'

    # CharField(max_length=120, verbose_name='Файл картинки') 2-й вариант, если слизать не получится...
    img = models.CharField(max_length=120, verbose_name='Файл картинки')
    # url = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Выберите маршрут', related_name='urls')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    alt = models.TextField(verbose_name='Подсказка')
    index = models.IntegerField(verbose_name='Индекс')
    objects = models.Model

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
