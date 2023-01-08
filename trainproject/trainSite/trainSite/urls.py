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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/teacher/', TeacherAPI.TeacherAPIListCreate.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/teacher/<int:pk>/',
         TeacherAPI.TeacherAPIUpdateDestroyRetrieve.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/subject/', SubjectAPI.SubjectAPIListCreate.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/subject/<int:pk>/',
         SubjectAPI.SubjectAPIUpdateDestroyRetrieve.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/student/', StudentAPI.StudentAPIListCreate.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/student/<int:pk>/',
         StudentAPI.StudentAPIUpdateDestroyRetrieve.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/statement/', StatementAPI.StatementAPIListCreate.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/statement/<int:pk>/',
         StatementAPI.StatementAPIUpdateDestroyRetrieve.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('api/v1/offices/', OfficesAPI.OfficesAPIListCreate.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/offices/<int:pk>/',
         OfficesAPI.OfficesAPIUpdateDestroyRetrieve.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
