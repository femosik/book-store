from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.show_categories),
    path('categories/<int:category_id>/',
        views.show_category_detail)
]
