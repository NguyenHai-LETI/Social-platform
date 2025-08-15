from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Chuyển hướng đến trang đăng nhập
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required  # Đảm bảo người dùng đã đăng nhập
def profile_update(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Chuyển hướng đến trang hồ sơ
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/profile_update.html', {'form': form})