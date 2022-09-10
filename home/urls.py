from django.urls import path
from . import views

urlpatterns = [
    path('', views.sayhello,name='home'),
    path('detail/<int:id_user>/', views.deatil, name='detail'),
    path('delete/<int:id_user>/', views.delete, name='delete'),
    path('update/<int:id_user>/', views.update, name='update'),
    path('create/', views.create, name='create'),
]
