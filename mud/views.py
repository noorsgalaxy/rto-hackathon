# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required

def get_or_none(m,**kwargs):
    try:
        return m.objects.get(**kwargs)
    except:
        return None

'''
@login_required(login_url = '/accounts/login/')
def get_info(request):
    pdetail_i = get_object_or_404(PersonalDetail, user = request.user)
    permanentadd_i = PermanentAdd.objects.get(user_personal = pdetail_i)
    if request.method == 'POST':
        presentadd = PresentAddForm(request.POST,instance=presentadd_i)
        vdetails = VehicleDetailsForm(request.POST,instance=vdetails_i)
        if all([presentadd.is_valid(), vdetails.is_valid()]):
            vdetails = vdetails.save(commit=False)
            vdetails.owner = pdetail_i
            vdetails.save()
            presentadd = presentadd.save(commit=False)
            presentadd.vehicle = vdetails
            presentadd.save()

            return HttpResponseRedirect('/mud/userdash/%s/' %(vdetails.chassis_no))
        else:
            return HttpResponseRedirect('erere')

    else:
        pdetail_f = pdetail_i
        permanent_f = permanentadd_i
        vdetails_f = VehicleDetailsForm(instance=vdetails_i)
        presentadd_f = PresentAddForm(instance=presentadd_i)
    return render(request, 'mud/NewVehicleRegistrationPage.html', {'pdetail_f': pdetail_f,'user': request.user,'presentadd_f': presentadd_f,'vdetails_f': vdetails_f,'permanent_f':permanent_f})
'''

@login_required(login_url = '/accounts/login/')
def reg(request,purpose):
    vdetails_i = None
    presentadd_i = None
    if request.method == 'GET':
        if purpose=='new':
            pdetail_i = get_or_none(PersonalDetail, user = request.user)
            permanentadd_i = get_or_none(PermanentAdd, user_personal = pdetail_i.aadhar_no)
            if not pdetail_i:
                return HttpResponseRedirect('/mud/pdetails')
        else:
            pdetail_i = get_or_none(PersonalDetail, user = request.user)
            permanentadd_i = get_or_none(PermanentAdd,user_personal = pdetail_i)
            vdetails_i = get_or_none(VehicleDetails, chassis_no=purpose)
            presentadd_i = get_or_none(PresentAdd, vehicle = vdetails_i)
    if request.method == 'POST':
        pdetail_i = get_or_none(PersonalDetail, user = request.user)
        vdetails_i = get_or_none(VehicleDetails, chassis_no=purpose)
        presentadd_i = get_or_none(PresentAdd, vehicle = vdetails_i)
        presentadd = PresentAddForm(request.POST,instance=presentadd_i)
        vdetails = VehicleDetailsForm(request.POST,instance=vdetails_i)
        if all([presentadd.is_valid(), vdetails.is_valid()]):
            vdetails = vdetails.save(commit=False)
            vdetails.owner = pdetail_i
            vdetails.save()
            presentadd = presentadd.save(commit=False)
            presentadd.vehicle = vdetails
            presentadd.save()

            return HttpResponseRedirect('/mud/userdash/%s/' %(vdetails.chassis_no))
        else:
            return HttpResponseRedirect('erere')

    pdetail_f = pdetail_i
    permanent_f = permanentadd_i
    vdetails_f = VehicleDetailsForm(instance=vdetails_i)
    presentadd_f = PresentAddForm(instance=presentadd_i)

    return render(request, 'mud/NewVehicleRegistrationPage.html', {'pdetail_f': pdetail_f,'user': request.user,'presentadd_f': presentadd_f,'vdetails_f': vdetails_f,'permanent_f':permanent_f})



@login_required(login_url = '/accounts/login/')
def pdetails(request):
    if request.method == 'POST':
        pdetail = PersonalDetailForm(request.POST)
        permanentadd = PermanentAddForm(request.POST)
        if all([pdetail.is_valid(), permanentadd.is_valid()]):
            pdetail = pdetail.save(commit=False)
            pdetail.user = request.user
            pdetail.save()
            permanentadd = permanentadd.save(commit=False)
            permanentadd.user_personal = pdetail
            permanentadd.save()
            print('goingg to save')

            return HttpResponseRedirect('/mud/newregistration/%s'%('new'))
        else:
            return HttpResponseRedirect('errrrrrr')
    else:
        pdetail_f = PersonalDetailForm()
        permanent_f = PermanentAddForm()

    return render(request, 'mud/UserBasicDetail.html', {'pdetail_f':pdetail_f,'permanentadd_f':permanent_f,'user':request.user})



@login_required(login_url = '/accounts/login/')
def accident_info(request,v_no):
    print v_no
    vdetails_i = get_object_or_404(VehicleDetails, registration_no=v_no)
#        vdetails_i = VehicleDetails.objects.get(registration_no=v_no)
    presentadd_i = get_object_or_404(PresentAdd, vehicle = vdetails_i)
    pdetail_i = vdetails_i.owner
    permanentadd_i = get_object_or_404(PermanentAdd, user_personal = pdetail_i)
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
        pdetail_f = pdetail_i
        permanent_f = permanentadd_i
        vdetails_f = vdetails_i
        presentadd_f = presentadd_i
        pollution_f  =PollutionCenterForm()

        return render(request, 'mud/PollutionControlUnit.html', {'pdetail_f': pdetail_f,'pollution_f':pollution_f,'presentadd_f': presentadd_f,'vdetails_f': vdetails_f,'permanent_f':permanent_f})


@login_required(login_url = '/accounts/login/')
def user_dashboard(request):
    puser_f = get_or_none(PersonalDetail,user = request.user)
    vno_f = VehicleDetails.objects.filter(owner = puser_f.aadhar_no)
    return render(request, 'mud/UserDashboard.html', {'puser_f':puser_f,'vno_f':vno_f,'user_name':request.user})


@login_required(login_url = '/accounts/login/')
def vehicle_details(request,cs_no):
    vdetails_i = get_object_or_404(VehicleDetails, chassis_no=cs_no)
    present_i = get_object_or_404(PresentAdd, vehicle=cs_no)
    vdetails_f = vdetails_i
    present_f = present_i
    return render(request, 'mud/UserDashboardVechiclesDetail.html', {'vdetails_f':vdetails_f,'present_f':present_f })



def main_page(request):
    return render(request, 'mud/MainPage.html')

def police_dashboard(request):
    vno = request.GET.get("vechicle-number") 
    if not vno:

        return render(request, 'mud/PoliceDashboard.html')
    else:
        return HttpResponseRedirect('/mud/police/'+str(vno))
