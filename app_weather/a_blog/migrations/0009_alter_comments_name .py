# Generated by Django 4.1.3 on 2022-12-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0008_alter_comments_text_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.TextField(max_length=50, verbose_name='имя'),
        ),
    ]
