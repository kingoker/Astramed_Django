from random import choices

from django.contrib.auth.models import User
from django.db import models


class Photos(models.Model):
    Photo_Type = [
        ('About', 'О нас'),
        ('Main', 'Главная')
    ]
    photo = models.ImageField(upload_to='img/', verbose_name='Фото')
    title = models.CharField(max_length=50, choices=Photo_Type)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.title


class Links(models.Model):
    Link_Type = [
        ('Instagram', 'Инстаграм'),
        ('Telegram', 'Телеграм'),
        ('Facebook', 'Фейсбук'),
    ]
    links = models.CharField(max_length=50, verbose_name='Ссылки')
    title = models.CharField(max_length=50, choices=Link_Type)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.title


class Services(models.Model):
    photo = models.ImageField(upload_to='service/', verbose_name='Фото')
    type = models.CharField(max_length=255, verbose_name='Тип услуги')
    doctor = models.CharField(max_length=255, default='врач-терапевт', verbose_name='Прием ведет')
    title = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.type


class Employee(models.Model):
    photo = models.ImageField(upload_to='employee/', verbose_name='Фото')
    name = models.CharField(max_length=255, verbose_name='ФИО')
    title = models.CharField(max_length=255, verbose_name='Должность')
    quote = models.CharField(max_length=255, verbose_name='Цитата')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    description = models.TextField(verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Users(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    photo = models.ImageField(upload_to='blogs/',  verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, verbose_name='Время')
    links = models.TextField(verbose_name='Скрытые ссылки')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title
