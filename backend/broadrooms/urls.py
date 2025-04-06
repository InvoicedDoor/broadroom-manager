from rest_framework import routers
from broadrooms import views

router = routers.DefaultRouter()

router.register('api/broadrooms', views.BroadroomView, 'broadrooms')

urlpatterns = router.urls