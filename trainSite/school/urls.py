from django.contrib import admin
from django.urls import path

from school.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('teacher/',
         TeacherView.as_view({'get': 'list', 'post': 'create'})),
    path('teacher/<int:pk>/',
         TeacherView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('subject/',
         SubjectView.as_view({'get': 'list', 'post': 'create'})),
    path('subject/<int:pk>/',
         SubjectView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('student/',
         StudentView.as_view({'get': 'list', 'post': 'create'})),
    path('student/<int:pk>/',
         StudentView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('statement/',
         StatementView.as_view({'get': 'list', 'post': 'create'})),
    path('statement/<int:pk>/',
         StatementView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    path('offices/',
         OfficesView.as_view({'get': 'list', 'post': 'create'})),
    path('offices/<int:pk>/',
         OfficesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
