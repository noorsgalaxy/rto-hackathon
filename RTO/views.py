# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import personal_detail
from .forms import info

def detail(request, aadhar_no):
    try:
        output = personal_detail.objects.get(pk=aadhar_no)
    except personal_detail.DoesNotExist:
        raise Http404("Personal Detail does not exit")
    return render(request,'RTO/detail.html',{'personal_detail': output})

def get_info(request):
    if request.method == 'POST':
        form = info(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.usern = request.user
            data.save()
            return HttpResponseRedirect('/')
    else:
        form = info()
    return render(request, 'RTO/info.html', {'form': form})



# Create your views here.
