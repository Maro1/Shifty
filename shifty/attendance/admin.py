from django.contrib import admin

from .models import RFIDUser, Attendance

admin.site.register(RFIDUser)
admin.site.register(Attendance)
