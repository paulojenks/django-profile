from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from . import models


class ProfileForm(forms.ModelForm):
    confirm_email = forms.EmailField(max_length=100, label='Confirm Email')
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birth_date = forms.DateField(input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'email', 'confirm_email', 'birth_date', 'bio', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('confirm_email')

        if email != verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = models.User
        fields = ['password1', 'password2']

    def clean(self):
        user = self.user
        old_password = self.cleaned_data['old_password']
        new_password = self.cleaned_data['new_password1']
        if new_password == old_password:
            raise forms.ValidationError(
                'Cannot use previous password'
            )
        first_name = user.first_name.lower()
        last_name = user.last_name.lower()
        username = user.username.lower()

        if (first_name or last_name or username) in new_password.lower():
            raise forms.ValidationError(
                'Password cannot contain username, last name or first name'
            )

        user.check_password(new_password)
