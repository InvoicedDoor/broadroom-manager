from rest_framework import routers
from broadrooms import views

router = routers.DefaultRouter()

router.register('api/users', views.BroadroomView, 'users')

urlpatterns = router.urls