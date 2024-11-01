from django.shortcuts import render
from django.http import HttpResponse

users = ['Jeny', 'German', 'Anton', 'Olga']
list_errors = {
    'ваш пароли не совпадают': 'password',
    'Ваше имя уже занято': 'username',
    'Ваш возраст не позвляет нам дать вам возможность зарегестрироваться на этот сайт': 'age',
}



def main(reqwest):
    if reqwest.method == 'POST':
        username = reqwest.POST.get('username')
        password = reqwest.POST.get('password') == reqwest.POST.get('repeat_password')
        age = reqwest.POST.get('age')
        if username in users:
            return HttpResponse(f'Это имя уже занято - {username}')
        elif not password:
            return HttpResponse(f'Пароли не совпадают')
        elif int(age) < 18:
            return HttpResponse('Ваш возраст не позволяет нам дать возможность вам зарегестрироваться на этом сайте')
        else:
            users.append(username)
            print(f'Новое имя - {username}')
            print(f'Пароль - {password}')
            print(f'Возраст - {age}')
            return HttpResponse(f'Вы успешно зарегестрировались {username}!')

    return render(reqwest, 'registration_page.html')


