from django.contrib import admin
from step.models import Warehouse, Preparing, InUse, Retired

# Register your models here.

admin.site.register(Warehouse)
admin.site.register(Preparing)
admin.site.register(InUse)
admin.site.register(Retired)