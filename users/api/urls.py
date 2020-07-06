from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.api.views import user_add, logout
# from .views import GroupViewSet
# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('register', user_add, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('logout', logout, name="logout"),
]

# urlpatterns += router.urls
