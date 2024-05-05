from datetime import datetime
from django.db import models # type: ignore

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Message(models.Model):
    value=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=100)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    def __str__(self):
        return self.user