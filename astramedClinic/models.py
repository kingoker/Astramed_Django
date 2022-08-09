from random import choices

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


class Services(models.Model):
    photo = models.ImageField(upload_to='service/', verbose_name='Фото')
    type = models.CharField(max_length=255, verbose_name='Тип услуги')
    doctor = models.CharField(max_length=255,default='врач-терапевт', verbose_name='Прием ведет')
    title = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Employee(models.Model):
    photo = models.ImageField(upload_to='employee/', verbose_name='Фото')
    name = models.CharField(max_length=255, verbose_name='ФИО')
    title = models.CharField(max_length=255, verbose_name='Должность')
    quote = models.CharField(max_length=255, verbose_name='Цитата')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


