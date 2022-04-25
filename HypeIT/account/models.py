from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.city

class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department

class Staff(models.Model):
    fName = models.CharField(max_length=30)
    lName = models.CharField(max_length=50)
    email = models.EmailField(default='@hype.de')
    city = models.ForeignKey(to='City', on_delete=models.PROTECT)
    department = models.ForeignKey(to='Department', on_delete=models.Prefetch)
    active = models.BooleanField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.fName+' '+self.lName

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.user.username
