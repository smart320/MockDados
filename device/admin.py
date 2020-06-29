from django.contrib import admin
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag_meter', 'text', 'company', 'uuid', 'created_at', 'mac', 'ota_name')


admin.site.register(Device, DeviceAdmin)
