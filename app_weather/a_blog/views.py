from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms, models
from .forms import CommentForm
from .models import Blog
from django.views import View
from django.core.paginator import Paginator



class BlogView(View):
    '''вывод записей и пагинация'''
    def get(self, request):
        #blog = Blog.objects.all()
        blog = models.Blog.objects.prefetch_related('comments', 'author')
        p = Paginator(Blog.objects.prefetch_related('comments'), 2)
        page = request.GET.get('page')
        blogs = p.get_page(page)
        nums = "a" * blogs.paginator.num_pages
        return render(request, "blog/index_blog.html",
                      {"blog_list": blog,
                       "blogs": blogs,
                       "nums": nums}
                      )

class BlogDetail(View):
    """отдельная страница записи"""
    def get(self, request, pk):
        blog = Blog.objects.select_related().get(id=pk)
        return render(request, 'blog/BlogDetail.html',
                          {'blog': blog
                           }
                      )


class AddComments(View):
    """добавление комментов"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = self.request.user #Выводим автора коммента
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


"""pk - это сокращение от primary key(первичный ключ)
он уникальным образом определяет каждую запись в базе данных"""



def register(request):
    if request.method == "POST":
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.set_password(registration_form.cleaned_data["password"])
            new_user.save()
            models.Profile.objects.create(user=new_user)
            return render(
                request,
                "registration/registration_complete.html",
                {"new_user": new_user},
            )
        else:
            return HttpResponse("ой, что-то пошло не так( Попробуйте ещё раз ")

    registration_form = forms.RegistrationForm()
    return render(
        request,
        "registration/register.html",
        {"form": registration_form},)



