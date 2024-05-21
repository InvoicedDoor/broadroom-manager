from django.db import models

# Create your models here.
class Broadroom(models.Model):
    broadroom_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    available = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
