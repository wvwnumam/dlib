from django.shortcuts import render 
from django.http import HttpResponse

from .models import Book

def index(request):
    books = Book.objects.all()
    context = {
        'title': 'dlib | Digital Library',
        'heading': 'Start Reading!',
        'books': books,
    }
    return render(request, 'books/index.html', context)

def detail(request, input):
    book = Book.objects.get(slug=input)
    context = {
        'title': book.title,
        'category': book.category,
        'writer': book.writer,
        'synopsis': book.synopsis,
        'cover': book.cover,
        'filename': book.filename,
    }
    return render(request, 'books/detail.html', context)