from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'^(?P<aadhar_no>[0-9]*)/$', views.detail, name='detail'),
    url(r'^$', views.get_info, name= 'get_info'),
#    url(r'^police/ew/$', views.accident_info, name='accident_info'),
    url(r'^police/(?P<v_no>\w+)/$', views.accident_info, name='accident_info'),
    url(r'^pollution/(?P<v_no>\w+)/$', views.pollution_check, name='pollution_check'),
    url(r'^userdash/$', views.user_dashboard, name ='user_dashboard'),
    url(r'^userdash/(?P<vehicle_no>\w+)/$', views.vehicle_details, name = 'vehicle_details')
]

