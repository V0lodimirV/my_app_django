from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Blog(models.Model):
    """Пост.Данные"""
    title = models.CharField('Заголовок поста', max_length=150)
    #text_blog = models.TextField('Текст записи')
    text_blog = RichTextField(blank=True, null=True)
    author = models.CharField('Имя автора', max_length=50)
    date = models.DateField('дата поста')
    img = models.ImageField('Изображения', upload_to='image_blog/%Y')#папка в которой хранятся изображения

    class Meta:
        verbose_name = 'Запись' #читаемое человеком имя поля
        verbose_name_plural = 'Записи' # тоже самое но во множественном числе


    def __str__(self):
        return f'{self.title}, {self.author}, {self.date}'




class Comments(models.Model):
    """комменты"""
    email = models.EmailField()
    name = models.CharField('имя', max_length=50)
    #text_comments = models.TextField('Текст коментария', max_length=2000)
    text_comments = RichTextField(blank=True, null=True)
    post = models.ForeignKey(Blog, verbose_name='коментарий к посту', on_delete=models.CASCADE, related_name="comments")
    created = models.DateField('дата добавления', auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Комментарий' #читаемое человеком имя поля
        verbose_name_plural = 'Комментарии' # тоже самое но во множественном числе


    def __str__(self):
        return f'{self.name}, {self.post}, {self.text_comments},{self.created},{self.author}'




class Profile(models.Model):
    """профиль пользователя"""

    birthday = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return str(self.user)

