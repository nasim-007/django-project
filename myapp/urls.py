from django.urls import path, include
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.homepage, name='homepage')
]