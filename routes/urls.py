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
    path('details', views.details)
]
