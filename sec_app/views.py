import django
from django.shortcuts import render
from sec_app.models import Users
from sec_app.form import UsersForm

# Create your views here.


def index(request):
    return render(request, 'sec_app/Home.html')


def users(request):
    Users.objects.all()
    values = {'users': Users.objects.all()}
    return render(request, 'sec_app/users.html', context=values)


def create_user(request):
    form = UsersForm()
    if request.method == "POST":
        form = UsersForm(request.POST)

        if form.is_valid():
            form.save(True)
            return users(request)

    return render(request, 'sec_app/create_user.html', {'form': form})
