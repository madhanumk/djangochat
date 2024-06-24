from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=15)
    is_active = models.BooleanField(default=False)
    


