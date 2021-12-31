from django.urls import path
from . import views

app_name = 'author'
urlpatterns = [
    path('register/', views.author_register, name='register'),
    path('login/', views.author_login, name='login')

]
