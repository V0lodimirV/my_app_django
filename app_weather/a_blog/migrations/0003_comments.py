# Generated by Django 4.1.3 on 2022-12-11 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0002_blog_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('text_comments', models.TextField(max_length=2000, verbose_name='Текст коментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_blog.blog', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]