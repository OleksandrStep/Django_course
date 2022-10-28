from django.shortcuts import render
from . import forms
# Create your views here.


def index(request):
    return render(request, "forms/Index.html")


def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validated")
            print(f'Name: {form.cleaned_data["name"]}')
            print(f'Email: {form.cleaned_data["email"]}')
            print(f'Text: {form.cleaned_data["text"]}')
            print(form.cleaned_data)

    return render(request, 'forms/form_page.html', {'form': form})
