from django.urls import path
from app_Nordestina.views import home, create, store, painel, logina, dashView

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('dash/', dashView, name='dashView'),
    path('store/', store, name='store'),
    path('painel/', painel, name='painel'),
    path('login/', logina, name= 'logina'),
]
