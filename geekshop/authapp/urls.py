from django.urls import path

#import authapp.views as authapp
from authapp.views import login, registration, logout, profile

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name = 'logout')
]