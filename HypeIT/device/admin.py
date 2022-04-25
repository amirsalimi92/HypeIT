from django.contrib import admin
from device.models import Brand, Os, Cpu, Ram, Vga
from device.models import Pc

# Register your models here.

admin.site.register(Brand)
admin.site.register(Os)
admin.site.register(Cpu)
admin.site.register(Ram)
admin.site.register(Vga)
admin.site.register(Pc)
#admin.site.register(Mobile)