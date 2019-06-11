from django.contrib.auth.models import User
from django import forms


#all we do here is make blueprint that will be used when will ever we will make forms
class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']