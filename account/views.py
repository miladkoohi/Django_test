from django.shortcuts import render, redirect
from .froms import UserRegisterFrom
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            f = form.cleaned_data
            User.objects.create_user(f['username'], f['email'], f['password'])
            messages.success(request, 'ایجاد شد به به م ')
            return redirect('home')
    else:
        form = UserRegisterFrom()
        return render(request, 'register.html', {'form': form})
