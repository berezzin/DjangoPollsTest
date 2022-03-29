from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_polls, name='hello_polls'),
]

