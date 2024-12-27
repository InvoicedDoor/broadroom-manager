from auth_users.views import AuthUsersView 
from django.urls import re_path, path
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/auth', AuthUsersView, basename='auth')

urlpatterns = router.urls