from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.show_books),
    path('books/<int:book_id>/',
        views.show_book_detail)
]
