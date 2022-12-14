"""dvap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path, include
from application import views as app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/' , app_views.home, name='home'),
    path('order/', app_views.order, name='order'),
    path('order/add_order/', app_views.add_order, name='add_order'),
    path('done_order/', app_views.done_order, name='done_order'),
    path('comments/', app_views.comments, name='comments'),
    path('comments/<int:id>', app_views.comment, name='comment'),
    path('comments/add_comment/', app_views.add_comment, name='add_comment'),
    
]

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #автоматическое добавление изображений в urlpatterns
