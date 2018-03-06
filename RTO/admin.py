# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import personal_detail, vehicle_detail, pollution_check, police_officer

admin.site.register(personal_detail)
admin.site.register(vehicle_detail)
admin.site.register(pollution_check)
admin.site.register(police_officer)

# Register your models here.
