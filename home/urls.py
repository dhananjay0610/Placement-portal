
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('student',views.student,name='student'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('recruitment',views.recruitment,name='recruitment'),
    path('handleApplication',views.handleApplication),
    path('<str:slug>/', views.blog, name='blog'),
    path('signup', views.handlesignup, name="handlesignup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name='logout'),
    path('studentInfo',views.studentInfo,name='studentInfo'),
]
