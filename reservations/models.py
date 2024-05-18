from django.db import models

# Create your models here.
class Reservation(models.Model):
    broadrooms_id = models.ForeignKey('')
    users_id = models.ForeignKey('')
    start_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(null=False)
    active = models.BooleanField(default=True)