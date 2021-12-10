from django.urls import path

#import authapp.views as authapp
from authapp.views import login, UserRegistrationCreateView, logout, UserUpdateView

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', UserRegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('logout/', logout, name = 'logout')
]