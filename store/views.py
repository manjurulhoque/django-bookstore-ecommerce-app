from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View

# Create your views here.

from .models import Book
from .forms import UserForm


@login_required(login_url='/store/login')
def index(request):
    if request.user.is_authenticated():
        books = Book.objects.all()
        context = {
            'books': books
        }
        return render(request, 'index.html', context)
    return render(request, 'login.html')


@login_required(login_url='/store/login')
def store(request):
    return render(request, 'store.html', {})


def login_user(request):
    if request.user.is_authenticated():
        return redirect('/store/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/store/login')


def register(request):
    if request.user.is_authenticated():
        return redirect('/store/')
    form = UserForm(request.POST or None)
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
    return render(request, 'registration.html', {})
