from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, JsonResponse


def posts(request):
    return HttpResponse('Посты')


def popular_posts(request):
    return HttpResponse('<h1>Популярные посты</h1>')


def last_posts(request):
    return HttpResponse('<h2>Последние посты</h2>')


def all_posts(request):
    dict = ['dota', 'minecrat', 'terraria', 'kostya']
    return HttpResponse(dict)


def like(request, id):
    likes = request.GET.get('likes', 0)
    comment = request.GET.get('likes', 0)
    return HttpResponse(f'{likes}, {comment}')


def login_password(request):
    login = request.GET.get('login', "Putin")
    password = request.GET.get('password', 12345)
    return HttpResponse(f'{login}, {password}')

def about(request):
    return HttpResponseRedirect("<p>Об этом</p>")

def contacts(request):
    return HttpResponsePermanentRedirect("<p>Контакты</p>")

def error_404(request):
    return HttpResponseNotFound('Загрузка страницы была завершена ошибкой')

def access(request, login, password):
    login = request.GET.get('login', 'admin')
    password = request.GET.get('password', 'admin')
    if login == 'admin' and password == 'admin':
        return HttpResponse('<p>Все норм</p>')
    else:
        return HttpResponse('<p>Неверные логин и пароль</p>')

def json(request):
    return JsonResponse({"name": "Sasha", "age": 17})

def set(request):
    username = request.GET.get('username', 'Sasha')
    response = HttpResponse(f"Hello {username}")
    response.set_cookie('username', username)
    return response

def get(request):
    username = request.COOKIES['username']
    return HttpResponse(f"Hello {username}")
