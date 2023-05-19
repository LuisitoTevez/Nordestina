from django.urls import path
from app_Nordestina import views

urlpatterns = [
   path('',views.home, name='home'),
]
