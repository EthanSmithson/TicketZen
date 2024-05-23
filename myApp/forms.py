from django.forms import ModelForm
from django import forms
from .models import User

class UploadForm(ModelForm):
    firstName = forms.TextInput()
    lastName = forms.TextInput()
    username = forms.TextInput()
    password = forms.TextInput()
    repassword = forms.TextInput()
    email = forms.TextInput()
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'username', 'password', 'repassword', 'email']
    
    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repassword = cleaned_data.get("repassword")
        if password == repassword:
            return password
        else:
            raise forms.ValidationError("Passwords do not match")