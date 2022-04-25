from django.contrib import admin
from account.models import City, Department, Staff, Profile

# Register your models here.

admin.site.register(City)
admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Profile)


