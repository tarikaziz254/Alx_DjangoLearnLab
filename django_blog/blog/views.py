from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'blog/register.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance = request.user )
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
        
    else:
        form = UserUpdateForm(instance = request.user)
    return render(request, 'blog/profile.html', {'form': form})