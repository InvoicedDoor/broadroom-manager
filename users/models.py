from typing import Any
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70, null=False)
    active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name