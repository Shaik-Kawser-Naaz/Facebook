from django.urls import path
from feed import views
urlpatterns=[
    path('home',views.func1,name="hp"),
    path('about',views.func2,name="ap"),
    path('contact',views.func3,name="cp"),
    path('posts',views.func4,name="pp"),
    path('login',views.func5,name="lp"),
    path('form',views.func6,name="fp"),
]