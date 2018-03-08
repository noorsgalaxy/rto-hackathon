from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'^(?P<aadhar_no>[0-9]*)/$', views.detail, name='detail'),
    url(r'^$', views.get_info, name= 'get_info')
]

