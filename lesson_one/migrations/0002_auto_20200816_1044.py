# Generated by Django 3.0.4 on 2020-08-16 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_one', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
