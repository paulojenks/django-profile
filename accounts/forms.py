from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from . import models


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'email', 'birth_date', 'bio', 'avatar']


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
