from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from books.models import Book
from categories.models import Category


def show_categories(request):
    categories = Category.objects.all()
    result = ''

    for category in categories:
        result += f'<body style="background-color: #262626;">' \
            f'<a href="/categories/{category.id}" style="' \
            f'color: #262626;' \
            f'background-color: white;' \
            f'font-size: 60px;' \
            f'margin-left: 30px;' \
            f'border-radius: 15px;' \
            f'padding: 10px;' \
            f'">{category.name}</a>'

    return HttpResponse(result)

def show_category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    books = category.books.all

    result = render_to_string('show_category_detail.html', {
        'title': category.name,
        'category': category,
        'books': books,
    })
    return HttpResponse(result)
