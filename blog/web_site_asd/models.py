from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(verbose_name='Заголовок статьи', max_length=155, unique=True)
    short_description = models.TextField(verbose_name='Краткое Описание', max_length=255)
    full_description = models.TextField(verbose_name='Полное Описание')
    photo = models.ImageField(verbose_name='Фото', upload_to='photos/articles/')
    views = models.IntegerField(verbose_name='Количество просмотров', default=0)
    created_at = models.DateTimeField(verbose_name='Дата создание', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='Дата обновление', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='articles')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
