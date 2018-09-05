from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Application)
admin.site.register(Report)
admin.site.register(ApplicationControlInfo)
admin.site.register(ReportControlInfo)
admin.site.register(MainLocationApplication)
