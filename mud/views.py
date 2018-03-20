# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

'''
def detail(request, aadhar_no):
    try:
        output = personal_detail.objects.get(pk=aadhar_no)
    except personal_detail.DoesNotExist:
        raise Http404("Personal Detail does not exit")
    return render(request,'RTO/detail.html',{'personal_detail': output})
'''

@login_required(login_url = '/accounts/login/')
def get_info(request):
    pdetail_i = None
    presentadd_i = None
    permanentadd_i = None
    vdetails_i = None
    try:
       pdetail_i = PersonalDetail.objects.get(user = request.user)
       permanentadd_i = PermanentAdd.objects.get(user_personal = pdetail_i)
       vdetails_i = VehicleDetails.objects.get(owner = pdetail_i)
       presentadd_i = PresentAdd.objects.get(vehicle = vdetails_i)
    except:
        pdetail_i = None
        presentadd_i = None
        permanentadd_i = None
        vdetails_i = None
    if request.method == 'POST':
        pdetail = PersonalDetailForm(request.POST,instance=pdetail_i)
        presentadd = PresentAddForm(request.POST,instance=presentadd_i)
        permanentadd = PermanentAddForm(request.POST,instance=permanentadd_i)
        vdetails = VehicleDetailsForm(request.POST,instance=vdetails_i)
        if all([pdetail.is_valid(), presentadd.is_valid(), permanentadd.is_valid(), vdetails.is_valid()]):
            pdetail = pdetail.save(commit=False)
            pdetail.user = request.user
            pdetail.save()
            permanentadd = permanentadd.save(commit=False)
            permanentadd.user_personal = pdetail
            permanentadd.save()
            vdetails = vdetails.save(commit=False)
            vdetails.owner = pdetail
            vdetails.save()
            presentadd = presentadd.save(commit=False)
            presentadd.vehicle = vdetails
            presentadd.save()

            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('erere')

    else:
        pdetail_f = PersonalDetailForm(instance=pdetail_i)
        permanent_f = PermanentAddForm(instance=permanentadd_i)
        vdetails_f = VehicleDetailsForm(instance=vdetails_i)
        presentadd_f = PresentAddForm(instance=presentadd_i)
        return render(request, 'mud/NewVehicleRegistrationPage.html', {'pdetail_f': pdetail_f,'user': request.user,'presentadd_f': presentadd_f,'vdetails_f': vdetails_f,'permanentadd_f':permanent_f})


@login_required(login_url = '/accounts/login/')
def accident_info(request,v_no):
    try:
        vdetails_i = VehicleDetails.objects.get(registration_no=v_no)
        presentadd_i = PresentAdd.objects.get(vehicle = vdetails_i)
        pdetail_i = vdetails_i.owner
        permanentadd_i = PermanentAdd.objects.get(user_personal = pdetail_i)
    except:
        pdetail_i = None
        presentadd_i = None
        permanentadd_i = None
        vdetails_i = None
    if request.method == 'POST':
        policeofficer = PoliceOfficerForm(request.POST)
        if policeofficer.is_valid() :
            policeofficer = policeofficer.save(commit=False)
            policeofficer.vehicle_no = vdetails_i
            policeofficer.save()
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('rr')
    else:
        pdetail_f = pdetail_i
        permanent_f = permanentadd_i
        vdetails_f = vdetails_i
        presentadd_f = presentadd_i
        police_f  =PoliceOfficerForm()

        return render(request, 'mud/PoliceControl.html', {'pdetail_f': pdetail_f,'police_f':police_f,'presentadd_f': presentadd_f,'vdetails_f': vdetails_f,'permanent_f':permanent_f})


@login_required(login_url = '/accounts/login/')
def pollution_check(request,v_no):
    try:
        vdetails_i = VehicleDetails.objects.get(registration_no=v_no)
        presentadd_i = PresentAdd.objects.get(vehicle = vdetails_i)
        pdetail_i = vdetails_i.owner
        permanentadd_i = PermanentAdd.objects.get(user_personal = pdetail_i)
    except:
        pdetail_i = None
        presentadd_i = None
        permanentadd_i = None
        vdetails_i = None
    if request.method == 'POST':
        pollutioncheck = PollutionCenterForm(request.POST)
        if pollutioncheck.is_valid() :
            pollutioncheck = pollutioncheck.save(commit=False)
            pollutioncheck.vehicle_no = vdetails_i
            pollutioncheck.save()
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('rr')
    else:
        pdetail_f = PersonalDetailForm(instance=pdetail_i)
        permanent_f = PermanentAddForm(instance=permanentadd_i)
        vdetails_f = VehicleDetailsForm(instance=vdetails_i)
        presentadd_f = PresentAddForm(instance=presentadd_i)
        pollution_f  =PollutionCenterForm()

        return render(request, 'mud/PollutionControlUnit.html', {'pdetail_f': pdetail_f,'pollution_f':pollution_f,'presentadd_f': presentadd_f,'vdetails_f': vdetails_f,'permanent_f':permanent_f})


@login_required(login_url = '/accounts/login/')
def user_dashboard(request):
    try:
        puser_i = PersonalDetail.objects.get(user = request.user)
#        print(puser_i.__dict__.values())
        owner_i = VehicleDetails.objects.filter(owner = puser_i.aadhar_no)
        vno_i = [VehicleDetails.objects.get(registration_no =i.registration_no) for i in owner_i]
    except:
        puser_i = None
        vno_i = None
    puser_f =  puser_i
    vno_f = vno_i
    return render(request, 'mud/UserDashboard.html', {'puser_f':puser_f,'vno_f':vno_f,'user_name':request.user})


@login_required(login_url = '/accounts/login/')
def vehicle_details(request,vehicle_no):
    try:
        vdetails_i = VehicleDetails.objects.get(registration_no=vehicle_no)
        print(vdetails_i)
        pollution_i = PollutionCenter.objects.get(v_no=vdetails_i.chassis_no)
        print(pollution_i)
    except:
        vdetails_i = None
        pollution_i = None
    vdetails_f = vdetails_i
    pollution_f = pollution_i
    return render(request, 'mud/UserDashboardVechiclesDetail.html', {'vdetails_f':vdetails_f,'pollution_f':pollution_f })
