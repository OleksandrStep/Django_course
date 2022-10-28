from django.forms import ModelForm
from sec_app.models import Users


class UsersForm(ModelForm):
    class Meta:
        model = Users
        # fields = "__all__"
        fields = ['first_name', 'last_name', 'email']
