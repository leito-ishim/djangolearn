from django.urls import path

#import authapp.views as authapp
from authapp.views import LoginListView, ProfileFormView, Logout, RegisterlistView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('registration/', RegisterlistView.as_view(), name='registration'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('logout/', Logout.as_view(), name = 'logout'),


    path('verify/<str:email>/<str:activate_key>/', RegisterlistView.verify, name='verify')
]