# Generated by Django 4.1 on 2022-09-05 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astramedClinic', '0038_alter_applications_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата закрытия заявки'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='number',
            field=models.CharField(max_length=255, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='status',
            field=models.CharField(choices=[('new', 'Новая'), ('process', 'В процессе'), ('done', 'Завершён')], default=('new', 'Новая'), max_length=50, verbose_name='Статус'),
        ),
    ]
