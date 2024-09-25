from django.urls import path
from . import views

urlpatterns = {
    path('', views.usermodel, name='usermodel'),
    path('book', views.bookmodel, name='bookmodel'),
}