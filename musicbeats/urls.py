#app levels
from django.urls import path
from . import views


urlpatterns = [
    path('songs/',views.songs, name='songs'),
    path('musicbeats/songs/<int:id>',views.songpost, name='songpost'),
    path('musicbeats/login/', views.login, name='login'),
    path('musicbeats/signup/', views.signup, name='signup'),

]