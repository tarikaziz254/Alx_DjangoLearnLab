from django.urls import path
from . import views
from .views import list_books
from . views import SignUpView
from django.contrib.auth.views import LoginView as auth_views
from django.contrib.auth.views import LogoutView as auth_views


urlpatterns = [
    path('books/', list_books, name = 'list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name = 'library_detail'),
    path('login/', auth_views.as_view(template_name = 'registratiion/login.html'), name = 'login'),
    path('logout/', auth_views.as_view(template_name = 'registration/logout.html'), name = 'logout'),
    path('signup/', SignUpView.as_view(), name = 'signup')
]