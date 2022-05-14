"""buffwild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings


handler404 = 'main.views.error_404_view'
handler500 = 'main.views.error_500_view'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cover, name='cover'),
    path('home/', views.home, name='home'),
    path('collection/', views.collection, name='collection'),
    path('collection/walletLookup/', views.walletLookup, name='walletLookup'),
    path('instructions/', views.instructions, name='instructions'),
    path('test/', views.test, name='test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
