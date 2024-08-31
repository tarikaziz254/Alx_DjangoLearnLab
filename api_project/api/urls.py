from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router = DefaultRouter()
router.register(r'book-list', BookViewSet)
urlpatterns = [
    path("book/", BookList.as_view(), name = "Book_list")
]