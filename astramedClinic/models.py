from random import choices

from django.contrib.auth.models import User
from django.db import models


class Photos(models.Model):
    Photo_Type = [
        ('About', 'О нас'),
        ('Main', 'Главная')
    ]
    photo = models.ImageField(upload_to='img/', verbose_name='Фото', max_length=255)
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
    photo = models.ImageField(upload_to='service/', verbose_name='Фото', max_length=255)
    type = models.CharField(max_length=255, verbose_name='Название терапии')
    doctor = models.CharField(max_length=255, default='врач-терапевт', verbose_name='Прием ведет')
    title = models.TextField(verbose_name='Описание')
    buttonname = models.CharField(max_length=255, default='Записаться на приём', verbose_name='Название кнопки')

    class Meta:
        verbose_name = 'Терапия'
        verbose_name_plural = 'Терапии'

    def __str__(self):
        return self.type


class UnderServices(models.Model):
    photo = models.ImageField(upload_to='underServices/', verbose_name='Фото', max_length=255)
    maintype = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, verbose_name='Главная терапия')
    undertype = models.CharField(max_length=255, default='название терапии', verbose_name='Название терапии')
    doctor = models.CharField(max_length=255, default='врач-терапевт', verbose_name='Прием ведет')
    title = models.TextField(verbose_name='Описание')
    buttonname = models.CharField(max_length=255, default='Записаться на приём', verbose_name='Название кнопки')

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'

    def __str__(self):
        return self.undertype


class Employee(models.Model):
    photo = models.ImageField(upload_to='employee/', verbose_name='Фото', max_length=255)
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


class CategoryBlog(models.Model):
    title = models.CharField(max_length=255, default='категория', verbose_name='Название')

    class Meta:
        verbose_name = 'Категория для блога'
        verbose_name_plural = 'Категории для блогов'

    def __str__(self):
        return self.title


class Blog(models.Model):
    author = models.CharField(max_length=255, verbose_name='Автор')
    title = models.TextField(max_length=255, verbose_name='Заголовок')
    category = models.ForeignKey(CategoryBlog, null=True, on_delete=models.CASCADE, verbose_name='Категория')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    photo = models.ImageField(upload_to='blogs/', verbose_name='Фото', max_length=255)
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True, verbose_name='Время')
    links = models.TextField(verbose_name='Скрытые ссылки')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.title


class MainModel(models.Model):
    philosophyTitle = models.CharField(max_length=255, verbose_name='Философия Заголовок')
    philosophy = models.CharField(max_length=255, verbose_name='Философия подзаголовок')
    philosophyPhoto = models.ImageField(upload_to='main/', verbose_name='Философия Фото', max_length=255)

    serviceTitle = models.CharField(max_length=255, verbose_name='Услуга Заголовок')
    serviceSubtitle = models.CharField(max_length=255, verbose_name='Услуга подзаголовок')
    serviceButtonSubtitle = models.CharField(max_length=255, verbose_name='Услуга нижний подзаголовок')

    teamTitle = models.CharField(max_length=255, verbose_name='Команда Заголовок')
    teamSubtitle = models.CharField(max_length=255, verbose_name='Команда подзаголовок')
    teamPhoto = models.ImageField(upload_to='main/', verbose_name='Команда Фото', max_length=255)

    faceToFaceTitle = models.CharField(max_length=255, verbose_name='F2F Заголовок')
    faceToFaceSubtitle = models.CharField(max_length=255, verbose_name='F2F подзаголовок')

    reviewTitle = models.CharField(max_length=255, verbose_name='Отзыв Заголовок')
    reviewSubtitle = models.CharField(max_length=255, verbose_name='Отзыв подзаголовок')
    reviewPhoto = models.ImageField(upload_to='main/', verbose_name='Отзыв Фото', max_length=255)

    BlogTitle = models.CharField(max_length=255, verbose_name='Блог Заголовок')
    BlogSubtitle = models.CharField(max_length=255, verbose_name='Блог подзаголовок')

    contactsTitle = models.CharField(max_length=255, verbose_name='Контакты Заголовок')

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

    def __str__(self):
        return "Главная"


class Info(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительные информации'

    def __str__(self):
        return self.title


class Applications(models.Model):
    name = models.CharField(max_length=255, verbose_name='ФИО')
    birth = models.CharField(max_length=255, verbose_name='Год рождения')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    therapy = models.CharField(max_length=255, default='Массаж', verbose_name='Терапия')
    number = models.CharField(max_length=255, verbose_name='number')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name


class PriceList(models.Model):
    priceFile = models.FileField(upload_to='priceList/', max_length=255, verbose_name='ФИО')

    class Meta:
        verbose_name = 'Прайс Лист'
        verbose_name_plural = 'Прайс Листы'


class Jobs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Должность')
    photo = models.ImageField(upload_to='jobs/', verbose_name='Фото', max_length=255)
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class Partners(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название партнера')
    photo = models.ImageField(upload_to='partners/', verbose_name='Фото', max_length=255)
    url = models.CharField(max_length=255,verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.title
