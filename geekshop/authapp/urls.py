from django.urls import path

#import authapp.views as authapp
from authapp.views import login, registration

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
]