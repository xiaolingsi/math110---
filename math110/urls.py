"""math110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('single_course/', views.single_course,name='single_course'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('video/',views.video,name='video'),
    path('addstuinfo/',views.add_edit_stuinfo,name='add_stu_info'),
    path('addteainfo/',views.add_edit_teainfo,name='add_tea_info'),
    path('choise_course/',views.choise_course,name='choise_course'),
    path('mycourse/',views.mycourse,name='mycourse'),
    path('allcourse/',views.allcourse,name='allcourse'),
    path('jump/',views.jump,name='jump'),
    path('search/',views.search,name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
