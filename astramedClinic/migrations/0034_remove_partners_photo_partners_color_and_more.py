# Generated by Django 4.1 on 2022-09-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astramedClinic', '0033_aboutpage_rename_mainmodel_mainpage_delete_photos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partners',
            name='photo',
        ),
        migrations.AddField(
            model_name='partners',
            name='color',
            field=models.CharField(choices=[('orange', 'Оранжевый'), ('yellow', 'Жёлтый'), ('grey', 'Серый')], default=('grey', 'Серый'), max_length=50, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='url',
            field=models.CharField(default='#', max_length=255, verbose_name='Ссылка'),
        ),
    ]
