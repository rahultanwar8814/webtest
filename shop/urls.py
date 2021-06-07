from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.index2,name="bnm"),
    path('signup2',views.loginUser,name="bnm2"),
    path('logout',views.logoutUser, name="logout"),

]
