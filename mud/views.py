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



# Create your views here.
