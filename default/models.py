from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=100,verbose_name="备忘事项")