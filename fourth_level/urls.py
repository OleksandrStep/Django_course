from django.urls import path
from fourth_level import views

app_name = "fourth_level"

urlpatterns = [
    path('', views.index, name="index"),
    path('other', views.other, name="other"),
    path('relative', views.relative_url, name="relative")
]
