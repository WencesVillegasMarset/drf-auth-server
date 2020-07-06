from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from users.api.views import user_add, logout
from .views import GroupViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('register', user_add, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('logout', logout, name="logout"),
    # path('groups/list', GroupViewSet.as_view({'get': 'list'}), name='group_list'),
    # path('groups/', GroupViewSet.as_view({'get': 'retrieve'}), name='group_retrieve'),
    # path('groups/', GroupViewSet.as_view({'get': 'retrieve'}), name='group_retrieve'),
    # path('groups/', GroupViewSet.as_view({'post': 'create'}), name='group_create'),

]

urlpatterns += router.urls
