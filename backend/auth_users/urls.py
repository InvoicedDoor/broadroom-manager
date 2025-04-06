from auth_users.views import AuthUsersView 
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'api/auth', AuthUsersView, basename='auth')

urlpatterns = router.urls