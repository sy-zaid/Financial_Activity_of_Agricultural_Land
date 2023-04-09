from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from Agriculture.models import signup
from django.core.validators import RegexValidator


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits "
                                         "allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=17)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("username", "email", 'phone', "password1", "password2")
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }