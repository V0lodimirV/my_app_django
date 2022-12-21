from django.contrib import admin
from .models import Blog, Comments, Profile

@admin.register(Blog)# регистрируем нашу модель в админке
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')


@admin.register(Comments)# регистрируем ещё одну модель в админке
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'text_comments')

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ("avatar", "user", "birthday")