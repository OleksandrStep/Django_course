from django.urls import path
from sec_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.users, name='users'),
    path('create_user', views.create_user, name='create_user')
]
