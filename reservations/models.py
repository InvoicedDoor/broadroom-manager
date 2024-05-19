from django.db import models
from users.models import User
from broadrooms.models import Broadroom
from services.time_counter import set_max_time

# Create your models here.
class Reservation(models.Model):
    broadrooms_id = models.ForeignKey(User, related_name='broadroom_id', on_delete=models.DO_NOTHING)
    users_id = models.ForeignKey(Broadroom, related_name='user_id', on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(null=False, default=set_max_time)
    active = models.BooleanField(default=True)