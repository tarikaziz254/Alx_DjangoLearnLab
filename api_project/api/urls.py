from django.urls import path
from . views import BookList

urlpatterns = [
    path("book/", BookList.as_view(), name = "Book_list")
]