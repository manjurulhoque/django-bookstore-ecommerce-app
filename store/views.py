from django.shortcuts import render

# Create your views here.

from .models import Book


def index(request):
    return render(request, 'index.html', {})


def store(request):
    count = Book.objects.all().count()
    context = {
        'count': count
    }
    return render(request, 'store.html', context)
