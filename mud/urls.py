from django.conf.urls import url

from . import views

urlpatterns = [
#    url(r'^(?P<aadhar_no>[0-9]*)/$', views.detail, name='detail'),
    url(r'^$', views.get_info, name= 'get_info'),
#    url(r'^police/ew/$', views.accident_info, name='accident_info'),
    url(r'^police/(?P<v_no>\w+)/$', views.accident_info, name='accident_info')
]

