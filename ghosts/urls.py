from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ghostnamepicker/', views.name_picker, name='name_picker'),
]
