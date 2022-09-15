from random import choices
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Links(models.Model):
    Link_Type = [
        ('instagram', 'Инстаграм'),
        ('telegram', 'Телеграм'),
        ('facebook', 'Фейсбук'),
    ]
    links = models.CharField(max_length=50, verbose_name='Ссылки')
    title = models.CharField(max_length=50, choices=Link_Type, verbose_name='Соц.Сеть')

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return self.title


class Services(models.Model):
    sort = models.IntegerField(null=True, blank=True, verbose_name='Позиция')
    photo = models.ImageField(upload_to='service/', verbose_name='Фото', max_length=255)
    type = models.CharField(max_length=255, verbose_name='Название терапии')
    doctor = models.CharField(max_length=255, default='врач-терапевт', verbose_name='Прием ведет')
    title = CKEditor5Field('Описание', config_name='extends')
    buttonname = models.CharField(max_length=255, default='Записаться на приём', verbose_name='Название кнопки')
    titleBeforeAfter = models.CharField(max_length=255, default='До и после', verbose_name='Заголовок фотографий')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Терапия'
        verbose_name_plural = 'Терапии'

    def __str__(self):
        return self.type


class ServicePhoto(models.Model):
    Photo = models.ImageField(upload_to='main/', default="", verbose_name='Фото услуги', max_length=255)
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    therapy = models.ForeignKey(Services, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Услуга')

    class Meta:
        verbose_name = 'Фотография услуги'
        verbose_name_plural = 'Фотографии услуги'

    def __str__(self):
        return 'фотография услуги'


class UnderServices(models.Model):
    photo = models.ImageField(upload_to='underServices/', verbose_name='Фото', max_length=255)
    maintype = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, verbose_name='Главная терапия')
    undertype = models.CharField(max_length=255, default='название терапии', verbose_name='Название терапии')
    doctor = models.CharField(max_length=255, default='врач-терапевт', verbose_name='Прием ведет')
    title = CKEditor5Field('Описание', config_name='extends')
    buttonname = models.CharField(max_length=255, default='Записаться на приём', verbose_name='Название кнопки')
    titleBeforeAfter = models.CharField(max_length=255, default='До и после', verbose_name='Заголовок фотографий')
    before = models.ImageField(upload_to='underServices/before/', null=True, blank=True, verbose_name='Фото До',
                               max_length=255)
    after = models.ImageField(upload_to='underServices/after/', null=True, blank=True, verbose_name='Фото После',
                              max_length=255)
    published = models.BooleanField(default=True, verbose_name='Опубликован')

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
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    published = models.BooleanField(default=True, verbose_name='Опубликован')
    description = models.TextField(verbose_name='Комментарий')
    doctor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Доктор')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

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
    description = CKEditor5Field('Описание', config_name='extends')
    date = models.DateField(auto_now_add=True, verbose_name='Время')
    links = CKEditor5Field('Скрытые ссылки', config_name='extends')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.title


class MainPage(models.Model):
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
        verbose_name = 'Страница Главная'
        verbose_name_plural = 'Страница Главная'

    def __str__(self):
        return "Страница Главная"


class CooperationPage(models.Model):
    CooperationTitle = models.CharField(max_length=255, verbose_name='Шапка')
    CooperationPageTitle = models.CharField(max_length=255, verbose_name='Заголовок')
    CooperationPageSubtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')

    class Meta:
        verbose_name = 'Страница сотрудничества'
        verbose_name_plural = 'Страница сотрудничества'

    def __str__(self):
        return "Страница сотрудничества"


class Info(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = CKEditor5Field('Описание', config_name='extends')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительные информации'

    def __str__(self):
        return self.title


class Applications(models.Model):
    statuses = [
        ('new', 'Новая'),
        ('process', 'В процессе'),
        ('done', 'Завершён'),
    ]
    status = models.CharField(max_length=50, choices=statuses, verbose_name='Статус', default=statuses[0])
    name = models.CharField(max_length=255, verbose_name='ФИО')
    birth = models.CharField(max_length=255, blank=True, null=True, verbose_name='Год рождения')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес')
    therapy = models.CharField(max_length=255, blank=True, null=True, default='Массаж', verbose_name='Терапия')
    number = models.CharField(max_length=255, verbose_name='Телефон')
    doctor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Доктор')
    userdate = models.DateTimeField(blank=True, null=True, verbose_name='Дата бронирования')
    time = models.TimeField(verbose_name='Время бронирования', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.name


class PriceList(models.Model):
    priceFile = models.FileField(upload_to='priceList/', max_length=255, verbose_name='ФИО')
    url = models.CharField(max_length=255, verbose_name='Ссылка', null=True, blank=True)

    class Meta:
        verbose_name = 'Прайс Лист'
        verbose_name_plural = 'Прайс Лист'

    def __str__(self):
        return 'Цены'


class Jobs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Должность')
    photo = models.ImageField(upload_to='jobs/', verbose_name='Фото', max_length=255)
    description = CKEditor5Field('Описание', config_name='extends')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class Partners(models.Model):
    color = [
        ('partner__orange', 'Оранжевый'),
        ('partner__yellow', 'Жёлтый'),
        ('partner__grey', 'Серый'),
    ]
    title = models.CharField(max_length=255, verbose_name='Название партнера')
    url = models.CharField(max_length=255, verbose_name='Ссылка', default="#")
    color = models.CharField(max_length=50, choices=color, verbose_name='Цвет', default=color[2])
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.title


class Contacs(models.Model):
    address = models.CharField(max_length=255, verbose_name='Наш адрес')
    worktime = models.CharField(max_length=255, verbose_name='Время работы')
    mainnumber = models.CharField(max_length=255, verbose_name='Номер телефона №1')
    secondnumber = models.CharField(max_length=255, default="", verbose_name='Номер телефона №2')
    telegram = models.CharField(max_length=255, verbose_name='Телеграм/SMS')
    email = models.CharField(max_length=255, verbose_name='Почта')
    transport = models.TextField(verbose_name='Общественный транспорт', default="")
    parking = models.TextField(verbose_name='Парковка', default="")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return 'Контакт'


class ServicesPage(models.Model):
    headerTitle = models.CharField(max_length=255, default="", verbose_name='Услуги Заголовок')
    faceToFaceTitle = models.CharField(max_length=255, default="", verbose_name='F2F Заголовок')
    faceToFaceSubtitle = models.CharField(max_length=255, default="", verbose_name='F2F подзаголовок')
    contactsTitle = models.CharField(max_length=255, default="", verbose_name='Контакты Заголовок')

    class Meta:
        verbose_name = 'Страница Услуги'
        verbose_name_plural = 'Страница Услуги'

    def __str__(self):
        return "Страница Услуги"


class PhilosBlog(models.Model):
    philosophyPhotoTitle = models.CharField(max_length=255, default="", verbose_name='Заголовок Фотографии')
    philosophydescription = models.CharField(max_length=255, default="", verbose_name='Описание фотографии')
    philosophyPhoto = models.ImageField(upload_to='main/', default="", verbose_name='Философия Фото', max_length=255)
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Фотография философии'
        verbose_name_plural = 'Фотографии философии'

    def __str__(self):
        return self.philosophyPhotoTitle


class AboutPage(models.Model):
    headerTitle = models.CharField(max_length=255, default="", verbose_name='О нас Заголовок')

    philosophyMainTitle = models.CharField(max_length=255, default="", verbose_name='Философия Заголовок')
    philosopyBlock = models.ForeignKey(PhilosBlog, null=True, blank=True, on_delete=models.CASCADE,
                                       verbose_name='Заголовок фотографии')

    teamTitle = models.CharField(max_length=255, default="", verbose_name='Команда Заголовок')
    teamSubtitle = models.CharField(max_length=255, default="", verbose_name='Команда подзаголовок', null=True,
                                    blank=True, )
    teamPhoto = models.ImageField(upload_to='main/', default="", verbose_name='Команда Фото', max_length=255)

    reviewTitle = models.CharField(max_length=255, default="", verbose_name='Отзыв Заголовок')
    reviewSubtitle = models.CharField(max_length=255, default="", verbose_name='Отзыв подзаголовок', null=True,
                                      blank=True, )
    reviewPhoto = models.ImageField(upload_to='main/', default="", verbose_name='Отзыв Фото', max_length=255)

    serviceTitle = models.CharField(max_length=255, default="", verbose_name='Услуга Заголовок')
    serviceSubtitle = models.CharField(max_length=255, default="", verbose_name='Услуга подзаголовок', null=True,
                                       blank=True, )

    contactsTitle = models.CharField(max_length=255, default="", verbose_name='Контакты Заголовок')

    class Meta:
        verbose_name = 'Страница О нас'
        verbose_name_plural = 'Страница О нас'

    def __str__(self):
        return "Страница О нас"
