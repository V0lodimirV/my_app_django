# Generated by Django 4.1.3 on 2022-12-23 19:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0006_comments_created_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text_blog',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
