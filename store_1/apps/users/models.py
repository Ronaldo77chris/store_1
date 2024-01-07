from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile=models.CharField(max_length=11,unique=True)
    class Meta:
        db_table='tb_user'
        verbose_name='user management'
    def __str__(self):
        return self.username
