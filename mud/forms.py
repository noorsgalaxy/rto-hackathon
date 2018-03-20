from django import forms
from mud.models import *
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
class PersonalDetailForm(forms.ModelForm):
    class Meta:
        model = PersonalDetail
        exclude = ['user']
        labels = {
            'user_name' : _('Your Full Name')
            }
class PresentAddForm(forms.ModelForm):
    class Meta:
        model = PresentAdd
        exclude = ['vehicle']
        labels = {
            'add1': _('Present Address')
            }
class PermanentAddForm(forms.ModelForm):
    class Meta:
        model = PermanentAdd
        exclude = ['user_personal']
        labels = {
            'add1': _('Permanent Address')
            }

class VehicleDetailsForm(forms.ModelForm):
    class Meta:
        model = VehicleDetails
        exclude = ['user_personal','owner','registration_no']


class PoliceOfficerForm(forms.ModelForm):
    accident_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = PoliceOfficer
        exclude = ['vehicle_no']

class PollutionCenterForm(forms.ModelForm):
    service_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    next_service_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = PollutionCenter
        exclude = ['v_no']
