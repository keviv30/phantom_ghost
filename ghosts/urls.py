from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/ghostuser/', views.name_picker, name='name_picker'),
    path('update/ghostname/', views.update_ghost_name, name='update_name'),
]
