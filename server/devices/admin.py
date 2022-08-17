from django.contrib import admin

from devices.models import *

admin.site.register(Device)
admin.site.register(ClassOfDevice)
admin.site.register(CompanyUse)
admin.site.register(IntervalCheck)
admin.site.register(CompanyCheck)
admin.site.register(TypeOfSi)
admin.site.register(SiCheck)
admin.site.register(IoCheck)
admin.site.register(IndicatorCheck)
admin.site.register(SkCheck)
