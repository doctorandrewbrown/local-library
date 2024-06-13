from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genres = Genre.objects.all().count()
    num_title_contains = Book.objects.filter(title__icontains='Wuthering').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_instances_reserved = BookInstance.objects.filter(status__exact='r').count()


    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_title_contains': num_title_contains,
        'num_genres': num_genres,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_instances_reserved': num_instances_reserved
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def books(request):
    """View function for list of all books."""
    book_list = Book.objects.all()
    context = {
        'book_list': book_list,
    }
    return render(request, 'book_list.html', context=context)


from django.views import generic


class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
