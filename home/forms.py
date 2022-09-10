from  django import  forms
from  .models import  User
class CreateUserFrom(forms.Form):
      firstname=forms.CharField(max_length=50,
                                label='نام'
                                )
      lastname=forms.CharField(max_length=50)
      email=forms.EmailField()
      phone=forms.CharField(min_length=11,max_length=11)
      username=forms.CharField()
class UserUpdateFrom(forms.ModelForm):
    class Meta:
        model=User
        fields=('frist_name','last_name','email','phone_number','user_name')