from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.decorators.cache import never_cache

from users.apps import UsersConfig
from users.views import (UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView,
                         UserTokenObtainPairView)

app_name = UsersConfig.name

urlpatterns = [
    #users urlpatterns
    path('', UserListAPIView.as_view(), name='user_list'),
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
]