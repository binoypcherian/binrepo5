from django.urls import path
from schoolapp import views

urlpatterns = [
    path('', views.fun1, name="fun1"),
    path('register/', views.fun2, name="fun2"),
    path('login/', views.fun3, name="fun3"),
    path('logout/', views.fun4, name="fun4"),
    path('forms/',views.fun5,name="fun5")
]