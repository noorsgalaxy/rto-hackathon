from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'^edit/$', views.get_info, name= 'get_info'),
    url(r'^newregistration/(?P<purpose>\w+)/$', views.reg, name = 'reg'),
    url(r'^pdetails/$', views.pdetails, name='pdetails'),
    url(r'^main/', views.main_page, name= 'main_page'),
    url(r'^police/(?P<v_no>\w+)/$', views.accident_info, name='accident_info'),
    url(r'^pollution/(?P<v_no>\w+)/$', views.pollution_check, name='pollution_check'),
    url(r'^userdash/$', views.user_dashboard, name ='user_dashboard'),
    url(r'^policedash/$', views.police_dashboard, name ='police_dashboard'),
    url(r'^userdash/(?P<cs_no>\w+)/$', views.vehicle_details, name = 'vehicle_details')
]

