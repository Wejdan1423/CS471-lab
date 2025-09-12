# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/index.html', {'books': books})

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'bookmodule/book.html', {'book': book})

