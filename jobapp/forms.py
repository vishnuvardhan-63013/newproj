from django import forms
from jobapp.models import submit,addpost,comment


class submitform(forms.ModelForm):
    class Meta:
        model = submit
        fields = ['jobtitle','first_name','last_name','email','phone']

class addform(forms.ModelForm):
    class Meta:
        model = addpost
        fields = "__all__"

class commentform(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['Content','Name','Email']


