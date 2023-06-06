from django import forms
from core.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import password_validators_help_text_html

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    password=forms.CharField(widget=forms.PasswordInput(),help_text=password_validation.password_validators_help_text_html())

    class Meta:
        model = User
        fields = ['f_name','l_name','email','password','confirm_password','zipcode']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(_("The two password fields did not match."))
            password_validation.validate_password(password,None)
        return confirm_password
    
    def password_validators_help_text_html(self):
        return ''