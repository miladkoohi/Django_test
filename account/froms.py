from django import forms


class UserRegisterFrom(forms.Form):
    username = forms.CharField(label='ایمیل')
    email = forms.EmailField(label='ایمیل')
    password = forms.CharField()
