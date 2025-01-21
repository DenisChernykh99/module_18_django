from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.

def sign_up_by_html(request):
    users = ['Denis', 'Katya']
    info = {}
    if request.method == 'POST':  # Проверяем метод коннекта с сервером
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # print(f'Username: {username}')
        # print(f'Password: {password}')
        # print(f'Repeat_Password: {repeat_password}')
        # (f'Age: {age}')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18!'
        elif username in users:
            info['error'] = 'Пользователь уже существует!'
        else:
            info['message'] = f'Приветствуем, {username}!'
            return render(request, 'registration_page.html', info)

    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = ['Denis', 'Katya']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                info['message'] = f'Приветствуем, {username}!'
                return render(request, 'registration_page.html', info)

    return render(request, 'registration_page.html', info)
