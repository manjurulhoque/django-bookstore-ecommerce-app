from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View

# Create your views here.

from .models import Book
from .forms import UserForm


def index(request):
    return render(request, 'index.html', {})


def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count
    }
    return render(request, 'store.html', context)


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
    return render(request, 'index.html', {})