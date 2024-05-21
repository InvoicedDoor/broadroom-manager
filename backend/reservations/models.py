from django.db import models
from users.models import User
from broadrooms.models import Broadroom
from services.time_counter import set_max_time

# Create your models here.
class Reservation(models.Model):
    broadrooms_id = models.ForeignKey(Broadroom, on_delete=models.CASCADE)
    users_id = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.TimeField(auto_now=False)
    finish_time = models.TimeField(null=False, default=set_max_time)
    active = models.BooleanField(default=True)