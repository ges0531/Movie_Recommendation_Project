from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
# from .models import User 이걸 안전하게 꺼내 쓰려면
from django.contrib.auth import login as auth_login, logout as auth_logout

# 회원가입용 Form, 인증(로그인)용 Form,
from .forms import CustomAuthenticationForm, CustomUserCreationForm

# 현재 Project에서 사용할 Uset 모델을 return 하는 함수
from django.contrib.auth import get_user_model
User = get_user_model()




@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form
    })

def logout(request):
    auth_logout(request)
    return redirect('/')


@require_GET
def user_page(request, user_id):
    # 특정 사람의 개인 페이지를 들어가고 싶은거
    user = get_object_or_404(User, id=user_id)
    return render(request, 'accounts/user_page.html', {
        'user_info': user,
    })


def follow(request, user_id):
    fan = request.user
    star = get_object_or_404(User, id=user_id)
    if fan != star:
        if star.fans.filter(id=fan.id).exists():
            star.fans.remove(fan)
        else:
            star.fans.add(fan)
    return redirect(star)
