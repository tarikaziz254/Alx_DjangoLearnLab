from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


router = DefaultRouter()
router.register(r'book-list', BookViewSet)
urlpatterns = [
    path("book-list", include(router.urls)),
    path("book/", BookList.as_view(), name = "Book_list")
]