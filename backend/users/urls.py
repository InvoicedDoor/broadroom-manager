from rest_framework import routers
from users import views

router = routers.DefaultRouter()

router.register('users', views.UserView, 'users')

urlpatterns = router.urls