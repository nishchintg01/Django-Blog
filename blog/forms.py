from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class new_form(UserCreationForm):
    email=forms.EmailField(required=True,initial='')
    name=forms.CharField(required=True,initial='')
    def __init__(self, *args, **kwargs):
        super(new_form, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['username'].help_text=''
        self.fields['password2'].help_text=''
    class Meta:
        model=User
        fields=['name','username','email','password1','password2']


class blog_data(forms.Form):
    pass
