#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
#def home(request):
#    return render(request, 'blog/home.html')
#def about(request):
 #   return render(request, 'blog/about.html', {'title': 'About'})
from django.shortcuts import render
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'engineering_books/home.html', {'books': books})

def about(request):
    return render(request, 'engineering_books/about.html', {'title': 'About Us'})
