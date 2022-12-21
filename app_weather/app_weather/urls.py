
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from a_blog.urls import urlpatterns_auth



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('a_weather.urls')),
    path('weather/', include('a_weather.urls')),
    path('index_exchange/', include('a_exchange.urls')),
    path('index_blog', include('a_blog.urls')),
    path('', include('a_blog.urls')),
    path('accounts/', include(urlpatterns_auth)),
    path('social-auth/', include('social_django.urls', namespace='social'))

]


"""нам будут доступны все медиа файлы.В режиме debug мы сможем перейти 
 к ним прямо в браузере, когда вылез какой-нибудь трейсбек ошибки, 
 и вообще это упрощает отладку приложения"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
