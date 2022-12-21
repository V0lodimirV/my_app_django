from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.BlogView.as_view()),#as_view потому что вьюшка реализована как класс а не функция
    path('<int:pk>/', views.BlogDetail.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),

]

""""<int:pk id номер каждой отдельной записи блога
pk- сокращение от primary key"""

urlpatterns_auth = [
    path("register/", view=views.register, name="register"),
    path("login/", view=auth_views.LoginView.as_view(), name="login"),
    path("logout/", view=auth_views.LogoutView.as_view(), name="logout"),

    path(
        "password_reset/",
        view=auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        view=auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        view=auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),
    path(
        "reset/done",
        view=auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
