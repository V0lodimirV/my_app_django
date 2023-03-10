# Generated by Django 4.1.3 on 2022-12-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок поста')),
                ('text_blog', models.TextField(verbose_name='Текст записи')),
                ('author', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('date', models.DateField(verbose_name='дата поста')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
