from django import forms
from mud.models import PersonalDetail, PresentAdd, PermanentAdd, VehicleDetails
from django.utils.translation import ugettext_lazy as _
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



        '''
    user_name = forms.CharField(label = 'Name', max_length = 20)
    father_name = forms.CharField(label = 'Father Name', max_length = 100)
    mother_name = forms.CharField(label = 'Mother Name', max_length = 100)
#    gender = forms.ChoiceField(label = 'Gender', widget=forms.Select(),choices = ('Male','Female'),required=True)
    permanent_address = forms.CharField(label = 'Permanent Address', max_length = 250)
    temporary_address = forms.CharField(label = 'Present Address',max_length = 250)
    duration_stay = forms.FloatField(label = 'Duration of stay at present address(years)')
    district = forms.CharField(label = 'District',max_length = 50)
    state = forms.CharField(label = 'State',max_length = 50)
    pan_no = forms.IntegerField(label = 'Pan Number')
    aadhar_no = forms.IntegerField(label =Number')
    mobile_no = forms.IntegerField(label = 'Mobile Number')
    email_id = forms.EmailField(label = 'Email id')'''
