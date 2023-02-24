from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='request_list'),
    path('register/', views.fun2, name="fun2"),
    path('login/', views.fun3, name="fun3"),
    path('logout/', views.fun4, name="fun4"),
    path('add/', views.StudentCreateView.as_view(), name='request_add'),
    path('<int:pk>/', views.StudentUpdateView.as_view(), name='request_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),
   ]