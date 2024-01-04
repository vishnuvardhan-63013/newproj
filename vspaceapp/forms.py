from django import forms
# from vishnuapp.models import profile
from jobapp.models import submit
from vspaceapp.models import subscribe

from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django_recaptcha.fields import ReCaptchaField


class userform(forms.ModelForm):
    password = forms.CharField(max_length=200,widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']
    captcha = ReCaptchaField()


class subscribeform(forms.ModelForm):
     class Meta:
            model = subscribe
            fields = "__all__"

# class form2(forms.ModelForm):
#     class Meta:
#         model = profile
#         fields = ['phone']

# class submitform(forms.ModelForm):
#     class Meta:
#         model = submit
#         fields = "__all__"