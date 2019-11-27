from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from .models import User
from django.views.decorators.http import require_http_methods, require_POST
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .forms import CustomAuthenticationForm, CustomUserCreationForm
from movies.models import Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            response = redirect('accounts:login')
            return response
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:user_list')
    
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:user_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:user_list')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/list.html', {
        'users': users,
    })

@login_required
def user_detail(request, user_id):
    user_info = get_object_or_404(User, id=user_id)
    reviews = Review.objects.filter(user=user_info)
    return render(request, 'accounts/detail.html', {
        'user_info': user_info,
        'reviews': reviews,
    })

@login_required
def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(User, id=user_id)
    if fan != star:
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)