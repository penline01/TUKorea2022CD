from django.urls import path
from . import views

# 프로젝트의 urls.py에 맵핑
urlpatterns = [
    path('', views.index, name='index')
]