# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PersonalDetail(models.Model):
    user = models.ForeignKey(User,default = "")
    user_name = models.CharField(max_length = 100)
    father_name = models.CharField(max_length = 100)
    mother_name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 6,choices=(('MALE','Male'),('FEMALE','Female')),default=1)
    pan_no = models.CharField(max_length = 20)
    aadhar_no = models.CharField(max_length = 12,primary_key = True)
    mobile_no = models.CharField(max_length = 13)
    email_id = models.EmailField(max_length = 25)


    def __str__(self):
        return str(self.aadhar_no)

class PermanentAdd(models.Model):
    user_personal = models.ForeignKey(PersonalDetail,default='')
    add1 = models.CharField(max_length = 200)
    state = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 6)

    def __str__(self):
        return str(self.user_personal)

class VehicleDetails(models.Model):
    vtype =  (
        ('PRIVATE','Private'),
        ('GOODS','Goods'),
        ('PASSENGER','Passenger'),
        ('SPECIAL', 'Special'),
    )
    vclass = (
        ('AMBULANCE','Ambulance'),
        ('CRANE','Crane'),
        ('FIRE FIGHTER','Fire Fighter'),
        ('HEAVY GOODS VEHICLE','Heavy Goods Vehicle'),
        ('L.M.V.(CAR)','L.M.V.(Car)'),
        ('L.M.V.(JEEP/GYPSY)','L.M.V.(Jeep/GYPSY)'),
        ('L.M.V.(VAN)','L.M.V.(Van)'),
        ('MOTOR CYCLE','Motor Cycle'),
        ('THREE WHEELER','Three Wheeler'),
        ('TRACTOR','Tractor'),
    )
    owner = models.ForeignKey(PersonalDetail,default='')
    dealer_name = models.CharField(max_length = 50)
    dealer_address = models.CharField(max_length = 250)
    vehicle_class = models.CharField(max_length = 20, choices = vclass, default = 8 )
    body_type = models.CharField(max_length = 20)
    vehicle_type =  models.CharField(max_length = 20, choices = vtype, default=1)
    company_name = models.CharField(max_length = 15)
    year_manufacture = models.IntegerField()
    numberof_cylinders = models.IntegerField()
    horse_power = models.IntegerField()
    cubic_capacity = models.IntegerField()
    chassis_no = models.CharField(primary_key = True , max_length = 50)
    engine_number = models.CharField(max_length = 100)
    seating_capacity = models.IntegerField()
    fuel_engine = models.CharField(max_length = 20)
    unladen_weight = models.IntegerField()
    body_color = models.CharField(max_length = 10)
    registration_no = models.CharField(max_length = 20, blank = True, default = "")

    def __str__(self):
        return  str(self.chassis_no)

class PoliceOfficer(models.Model):
    vehicle_no = models.ForeignKey(VehicleDetails, default='')
    accident_location = models.CharField(max_length = 20)
    accident_cause = models.CharField(max_length = 20)
    no_persons_injured = models.IntegerField()
    accident_date = models.DateField()

    def __str__(self):
        return str(self.vehicle_no)



class PresentAdd(models.Model):
    vehicle = models.ForeignKey(VehicleDetails,default='')
    add1 = models.CharField(max_length = 200)
    state = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 6)

    def __str__(self):
        return str(self.vehicle)




class PollutionCenter(models.Model):
    p_status = (
        ('GOOD','Good'),
        ('BAD','Bad')
    )
    v_no = models.ForeignKey(VehicleDetails, default='')
    service_date = models.DateField()
    next_service_date = models.DateField()
    total_distance = models.IntegerField()
    pollution_status = models.CharField(max_length = 4, choices=p_status, default=1)

    def __str__(self):
        return str(self.v_no)















