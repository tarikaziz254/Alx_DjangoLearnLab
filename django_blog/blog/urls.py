from django.urls import path
from .views import RegisterView, ProfileUpdateView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView, name = 'login'),
    path('logout/', LogoutView, name = 'logout'),
    path('profile/', ProfileUpdateView.as_view(), name = 'profile'),
]