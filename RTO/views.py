# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import personal_detail
from .forms import personal_info

def detail(request, aadhar_no):
    try:
        output = personal_detail.objects.get(pk=aadhar_no)
    except personal_detail.DoesNotExist:
        raise Http404("Personal Detail does not exit")
    return render(request,'RTO/detail.html',{'personal_detail': output})

def get_info(request):
    if request.method == 'POST':
        form = personal_info(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            personal_info_obj = personal_detail(user_name=data['user_name'],father_name=data['father_name'],mother_name=data['mother_name'],permanent_address=data['permanent_address'],temporary_address=data['temporary_address'],duration_stay=data['duration_stay'],district=data['district'],state=data['state'],pan_no=data['pan_no'],aadhar_no=data['aadhar_no'],mobile_no=data['mobile_no'],email_id=data['email_id'])
            personal_info_obj.save()
            return HttpResponseRedirect('')
    else:
        form = personal_info()
    return render(request, 'RTO/info.html', {'form': form})



# Create your views here.
