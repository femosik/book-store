from django.http import HttpResponse
from django.shortcuts import render

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
    result = f'<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">' \
        f'<span style="color: white;' \
        f'font-family: sans-serif;' \
        f'font-size: 42px;">{category.name} </span><i class="fas fa-backward"></i><hr><br>'

    books = category.books.all()
    for book in books:
        result += f'<body style="background-color: #262626;"><a href="/books/{book.id}" style="' \
            f'color: #262626;' \
            f'background-color: white;' \
            f'font-size: 60px;' \
            f'margin-left: 30px;' \
            f'border-radius: 15px;' \
            f'padding: 10px">{book.name}</a>'

    return HttpResponse(result)
