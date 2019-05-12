from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from books.models import Book


def show_books(request):
    books = Book.objects.all()
    result = ''

    for book in books:
        result += f'<a href="/books/{book.id}">{book.name}</a><br>'

    return HttpResponse(result)

def show_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    result = render_to_string('show_book_detail.html', {
        'title': book.name,
        'book': book,
    })

    return HttpResponse(result)
