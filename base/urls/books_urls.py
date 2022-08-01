from django.urls import include, path
from rest_framework import routers
from base.views import books_views as views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.get_books, name='books'),
    path('add/', views.add_book, name='book_add'),
    path('<str:pk>/', views.get_book, name='book'),
    path('<str:pk>/edit/', views.edit_book, name='book_edit'),
    path('<str:pk>/upload/', views.upload_book_image, name='book_upload'),
    path('<str:pk>/delete/', views.delete_book, name='book_delete'),
]