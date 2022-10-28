from django.urls import path
from forms.views import index, form_name_view


app_name = 'forms'

urlpatterns = [
    path('', index, name='index'),
    path('form', form_name_view, name='form_name_view')
]
