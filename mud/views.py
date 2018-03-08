# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import PersonalDetail
from .forms import PersonalDetailForm
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
    try:
        instance = PersonalDetail.objects.get(user = request.user)
    except PersonalDetail.DoesNotExist:
        instance = None
    if request.method == 'POST':
        form = PersonalDetailForm(request.POST,instance=instance)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return HttpResponseRedirect('')
    else:
        print instance
        form = PersonalDetailForm(instance=instance)
    return render(request, 'mud/info.html', {'form': form,'user':request.user})



# Create your views here.
