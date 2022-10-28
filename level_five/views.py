from django.shortcuts import render
from level_five.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, "level_five/index.html")


def sign_up(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            # if 'profile_pic' in request.FILES:
            #     print(request.FILES['profile_pic'], type(request.FILES['profile_pic']))
            #     profile.profile_pic = request.FILES['profile_pic']
            # print(profile.profile_pic)
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "level_five/sing_up.html", {'user_form': user_form,
                                                       'profile_form': profile_form,
                                                       'registered': registered})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('five:index'))
            else:
                HttpResponse("Account not active")
        else:
            print(f"Someone tried to login with username: {username}")
            return HttpResponse("invalid login details")
    else:
        return render(request, 'level_five/sign_in.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('five:index'))


@login_required
def users(request):
    return render(request, "level_five/users.html")
