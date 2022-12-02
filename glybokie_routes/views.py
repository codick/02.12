from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


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
    return HttpResponseRedirect("/posts")

def details(request):
    return HttpResponsePermanentRedirect("/")