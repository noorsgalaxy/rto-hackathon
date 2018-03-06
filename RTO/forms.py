from django import forms

class personal_info(forms.Form):

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
    aadhar_no = forms.IntegerField(label = 'Aadhar Number')
    mobile_no = forms.IntegerField(label = 'Mobile Number')
    email_id = forms.EmailField(label = 'Email id')


