from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   text = models.CharField(max_length=200)


   def __str__(self):
       return f'{self.pk}: {self.text}'
