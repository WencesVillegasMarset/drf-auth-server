from django.urls import path, include
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
    path('password-reset/', include(
        'django_rest_passwordreset.urls', namespace='password_reset')),
]

# urlpatterns += router.urls
