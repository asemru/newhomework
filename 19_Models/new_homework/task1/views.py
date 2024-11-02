from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

users = ['Jeny', 'German', 'Anton', 'Olga']
list_errors = {
    'ваш пароли не совпадают': 'password',
    'Ваше имя уже занято': 'username',
    'Ваш возраст не позвляет нам дать вам возможность зарегестрироваться на этот сайт': 'age',
}





def index(request):
    all_games = Games.objects.all()
    context = {
        'all': all_games
    }

    return render(request, 'videogames.html', context)


def main(reqwest):
    if reqwest.method == 'POST':
        username = reqwest.POST.get('username')
        password3 = reqwest.POST.get('password') == reqwest.POST.get('repeat_password')
        password2 = reqwest.POST.get('password')
        age = reqwest.POST.get('age')
        if username in users:
            return HttpResponse('Это имя уже занято')
        elif not password3:
            return HttpResponse(f'Пароли не совпадают')
        elif int(age) < 18:
            return HttpResponse('Ваш возраст не позволяет нам дать возможность вам зарегестрироваться на этом сайте')
        else:
            users.append(username)
            print(f'Новое имя - {username}')
            print(f'Пароль - {password3}')
            print(f'Возраст - {age}')
            #Games.objects.create(name=f"{username}", password=f"{password2}", age=f"{int(age)}")
            return render(reqwest, 'menu.html')

    return render(reqwest, 'registration_page.html')


