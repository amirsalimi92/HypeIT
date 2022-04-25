from random import choices
from django.db import models

# Create your models here.

class Brand(models.Model):
    brand = models.CharField(max_length=35)

    def __str__(self):
        return self.brand

class Os(models.Model):
    os = models.CharField(max_length=35)

    def __str__(self):
        return self.os

class Cpu(models.Model):
    cpu = models.CharField(max_length=75)

    def __str__(self):
        return self.cpu

class Ram(models.Model):
    ram = models.CharField(max_length=35)

    def __str__(self):
        return self.ram

class Vga(models.Model):
    vga = models.CharField(max_length=35)

    def __str__(self):
        return self.vga

class Pc(models.Model):
    nickName = models.CharField(max_length=100)
    brand = models.ForeignKey(to='Brand', on_delete=models.PROTECT)
    os = models.ForeignKey(to='Os', on_delete=models.PROTECT)
    
    type_of_device = (
        (1,'Laptop'),(2,'NUC'),(3,'Server'),(4,'PC'),(5,'All-in-One'),(6,'Other'),
    )

    type = models.IntegerField(choices= type_of_device)
    cpu = models.ForeignKey(to='Cpu', on_delete=models.PROTECT)
    ram = models.ForeignKey(to='Ram', on_delete=models.PROTECT)
    vga = models.ForeignKey(to='Vga', on_delete=models.PROTECT)
    storage = models.CharField(max_length=50)
    display = models.CharField(max_length=50, blank=True)
    other = models.TextField(blank=True)

    def __str__(self):
        return self.nickName

'''class Mobile(models.Model):  
    nickName = models.CharField(max_length=100)
    brand = models.ForeignKey(to='Brand', on_delete=models.PROTECT)
    storage = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    other = models.TextField(blank=True)

    def __str__(self):
        return self.nickName'''


