# Generated by Django 4.1 on 2022-08-09 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('astramedClinic', '0005_delete_links_delete_photos_delete_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('links', models.CharField(max_length=50, verbose_name='Ссылки')),
                ('title', models.CharField(choices=[('Instagram', 'Инстаграм'), ('Telegram', 'Телеграм'), ('Facebook', 'Фейсбук')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='img/', verbose_name='Фото')),
                ('title', models.CharField(choices=[('About', 'О нас'), ('Main', 'Главная')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='service/', verbose_name='Фото')),
                ('title', models.CharField(max_length=255, verbose_name='Описание')),
            ],
        ),
    ]
