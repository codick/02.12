from django.contrib import admin
from django.urls import path, include
from glybokie_routes import views


posts = [
    path('popular_posts', views.popular_posts),
    path('last_posts', views.last_posts),
    path('all_posts', views.all_posts),
    path('<int:id>', views.like),
]

urlpatterns = [
    path('posts/', include(posts)),
    path('login_password', views.login_password),
    path('about', views.about),
    path('contacts', views.contacts),
    path('error_404', views.error_404),
    path('access/', views.access),
    path('json', views.json),
    path('set', views.set),
    path('get', views.get)
]
