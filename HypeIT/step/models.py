from django.db import models
from device.models import Pc
from account.models import Profile, Staff
from django.contrib.auth.models import User

# Create your models here.


class Warehouse(models.Model):
    device = models.ForeignKey(to=Pc, on_delete=models.PROTECT)
    orderer = models.ForeignKey(to=User, on_delete=models.PROTECT)
    price = models.IntegerField()
    orderDate = models.DateField()
    
    next_step = (
        (1,'Not delivered'),(2,'Got it'),(3,'Idle'),(4,'Wait for the upgrade'),(5,'Wait for repairs'),(6,'Other'),
    )

    status = models.IntegerField(choices=next_step, default=1)
    serialNumber = models.CharField(max_length=50, default='Please change it after delivery')
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.device.nickName}   {self.serialNumber} ordered in: {self.orderDate}'


class Preparing(models.Model):
    device = models.OneToOneField(Warehouse, on_delete=models.PROTECT)
    domainName = models.CharField(max_length=25, unique=True)

    status_of_preparing = (
        (1,'Nothing'),(2,'Not complete'),(3,'Complete'),
    )

    status = models.IntegerField(choices=status_of_preparing, default=1)
    editor = models.ForeignKey(to=User, on_delete=models.PROTECT)
    comment = models.TextField(blank=True)
        

    def __str__(self):
        return f'{self.domainName}  status: {self.status}'


class InUse(models.Model):
    device = models.OneToOneField(Preparing, on_delete=models.PROTECT)

    status_of_preparing = (
        (1,'Nothing'),(2,'Not complete'),(3,'Complete'),
    )


    status = models.IntegerField(choices=status_of_preparing, default=1)
    staff = models.ForeignKey(to=Staff, on_delete=models.PROTECT)
    editor = models.ForeignKey(to=User, on_delete=models.PROTECT)
    date = models.DateField()
    comment = models.TextField(blank=True)


    def __str__(self):
        return f'{self.device.domainName} for {self.staff}'

class Retired(models.Model):
    device = models.OneToOneField(InUse, on_delete=models.PROTECT)

    status_of_retired = (
        (1,'Idle'),(2,'Recycling'),(3,'Other'),
    )

    status = models.IntegerField(choices=status_of_retired, default=1)
    date = models.DateField()
    comment = models.TextField(blank=True)



    def __str__(self):
        return f'{self.device.device.domainName} {self.status}'

