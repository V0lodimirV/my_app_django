# Generated by Django 4.1.3 on 2022-12-14 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='a_blog.blog', verbose_name='коментарии'),
        ),
    ]
