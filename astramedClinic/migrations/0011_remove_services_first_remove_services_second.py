# Generated by Django 4.1 on 2022-08-09 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astramedClinic', '0010_rename_main_services_first'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='first',
        ),
        migrations.RemoveField(
            model_name='services',
            name='second',
        ),
    ]
