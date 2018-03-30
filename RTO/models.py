# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class personal_detail(models.Model):
    user_name = models.CharField(max_length = 100,default='satya')
    father_name = models.CharField(max_length = 100,default='deep')
    mother_name = models.CharField(max_length = 100,default='satya')
#    gender = models.CharField(max_length = 6,choices=(('MALE','Male'),('FEMALE','Female')),default=1)
    permanent_address = models.CharField(max_length = 250,default='satya')
    temporary_address = models.CharField(max_length = 250,default='satya')
    district = models.CharField(max_length = 50,default='satya')
    state = models.CharField(max_length = 50,default='satya')
    duration_stay = models.FloatField(max_length = 4,default=0.0)
    pan_no = models.IntegerField(default = None)
    aadhar_no = models.IntegerField(primary_key = True)
    mobile_no = models.IntegerField(default=0)
    email_id = models.EmailField(max_length = 25,default='satya')


    def __str__(self):
        return str(self.aadhar_no)
'''
class vehicle_detail(models.Model):
    owner = models.ForeignKey(personal_detail)
    dealer_name = models.CharField(max_length = 50)
    dealer_address = models.CharField(max_length = 250)
    vehicle_class = models.CharField(max_length = 20)
    body_type = models.CharField(max_length = 20)
    vehicle_type =  models.CharField(max_length = 20)
    company_name = models.CharField(max_length = 15)
    year_manufacture = models.IntegerField()
    numberof_cylinders = models.IntegerField()
    horse_power = models.IntegerField()
    cubic_capacity = models.IntegerField()
    chassis_no = models.IntegerField(primary_key = True)
    engine_number = models.CharField(max_length = 100)
    seating_capacity = models.IntegerField()
    fuel_engine = models.CharField(max_length = 20)
    unladen_weight = models.IntegerField()
    body_color = models.CharField(max_length = 10)
    registration_no = models.CharField(max_length = 20, blank = True, default = "")

    def __str__(self):
        return  str(self.chassis_no)

class pollution_check(models.Model):
    user_name = models.CharField(max_length = 20)
    vehicle_no = models.ForeignKey(vehicle_detail)
    total_distance = models.IntegerField()
    pollution_status = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.vehicle_no)


class police_officer(models.Model):
    police_name = models.CharField(max_length = 20)
    vehicle_no = models.ForeignKey(vehicle_detail)
    accident_area = models.CharField(max_length = 20)
    accident_cause = models.CharField(max_length = 20)


    def __str__(self):
        return str(vehicle_no)
'''

















