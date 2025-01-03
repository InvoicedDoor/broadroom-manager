from rest_framework import routers
from reservations import views

router = routers.DefaultRouter()

router.register('reservations', views.ReservationView, 'reservations')

urlpatterns = router.urls