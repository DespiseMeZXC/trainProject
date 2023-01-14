"""trainSite URL Configuration

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
from django.contrib import admin
from django.urls import path

from school.views import *
from .yasg import urlpatterns as doc_urls 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/teacher/', TeacherView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/teacher/<int:pk>/',
         TeacherView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/subject/', SubjectView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/subject/<int:pk>/',
         SubjectView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/student/', StudentView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/student/<int:pk>/',
         StudentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/statement/', StatementView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/statement/<int:pk>/',
         StatementView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/offices/', OfficesView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/offices/<int:pk>/',
         OfficesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
urlpatterns += doc_urls
