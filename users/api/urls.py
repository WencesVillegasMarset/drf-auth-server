from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.api.views import registration_view, logout

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('logout', logout, name="logout")
]
