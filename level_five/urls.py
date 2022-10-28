from django.urls import path
from level_five import views

app_name = "five"

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_up', views.sign_up, name="sign_up"),
    path('sign_in', views.sign_in, name="sign_in"),
    path('logout', views.user_logout, name="logout"),
    path('users', views.users, name="users")
]
