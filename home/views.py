from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from .forms import CreateUserFrom, UserUpdateFrom


def sayhello(request):
    data = User.objects.all()
    return render(request, 'index.html', {'data': data})


def deatil(request, id_user):
    data = User.objects.get(id=id_user)
    return render(request, 'deatil.html', {'data': data})


def delete(request, id_user):
    data = User.objects.get(id=id_user).delete()
    messages.success(request, 'با موقیت حذف شد')
    return redirect('home')


def create(request):
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(frist_name=data['firstname'],
                                last_name=data['lastname'],
                                email=data['email'],
                                phone_number=data['phone'],
                                user_name=data['username']
                                )
            messages.success(request, 'ثبت شد به به م جان')
            return redirect('home')
    form = CreateUserFrom
    return render(request, 'create.html', {'form': form})


def update(request, id_user):
    user = User.objects.get(id=id_user)
    if request.method == 'POST':
        form = UserUpdateFrom(request.POST,instance=user)
        form.save()
        messages.success(request, 'اپدیت شد به به م ')
        return redirect('home')
    else:
        form = UserUpdateFrom(instance=user)
        return render(request, 'update.html', {'form': form})
