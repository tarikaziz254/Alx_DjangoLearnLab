from django.shortcuts import render
from . models import Book,  Library
from django.views.generic import DetailView

def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_book.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'