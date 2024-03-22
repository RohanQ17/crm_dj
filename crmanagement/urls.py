from django.urls import path
from . import views

urlpatterns = [
                path('', views.home, name='home'),
                path('register/', views.register_user, name='register'),
                path('logout/', views.logout_user, name='logout'),
                path('record/<int:pk>/', views.see_record, name='see_record'),
                path('delete_record/<int:pk>/', views.delete_record, name='delete_record')
               ]
