from django.http import HttpResponse
from django.template.loader import render_to_string

from books.models import Book
from categories.models import Category


def show_main_page(request):
    books = Book.objects.order_by('-id')[:5]
    categories = Category.objects.all()[:5]

    result = render_to_string('main.html', {
        'title': 'Books',
        'categories': categories,
        'books': books,
    })

    return HttpResponse(result)
