from django import forms

class info(forms.Form):
    user_name = forms.CharField(label = 'Name', max_length = 20)
    age = forms.IntegerField(label ='Age')
    gender = forms.CharField(label = 'Gender', max_length = 10)
    address = forms.CharField(label = 'Address', max_length = 100)
    email = forms.EmailField()


