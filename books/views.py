from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def show_books(request):
    books = Book.objects.all()
    result = ''

    for book in books:
        result += f'<a href="/books/{book.id}">{book.name}</a><br>'

    return HttpResponse(result)

def show_book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    result = (f'<body style="' 
        f'background-color: #262626">' 
        f'<h1 style="' 
        f'color: white;'  
        f'font-family: sans-serif;">{book.name}</h1>' 
        f'<div style="' 
        f'font-size: 20px;' 
        f'color: white;">{book.description}</div><br>' 
        f'<div style="font-family: sans-serif;'
        f' font-size: 30px;' 
        f' color: white;">Цена: {book.price} рублей</div>')

    return HttpResponse(result)
