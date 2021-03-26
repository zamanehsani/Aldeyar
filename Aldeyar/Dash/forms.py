from django import forms
from django.contrib.auth.models import User
from Dash.models import Profile
class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username']

class UserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'phone', 'address','photo']      