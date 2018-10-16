from django import forms
from django.contrib.auth.forms import PasswordChangeForm

import datetime

from . import models


class ProfileForm(forms.ModelForm):
    years = range(datetime.datetime.today().year - 100, datetime.datetime.today().year-13)  # year range for date
    email = forms.EmailField(max_length=100, label='Email')
    confirm_email = forms.EmailField(max_length=100, label='Confirm Email')
    avatar = forms.ImageField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"), years=years),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y'], required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'email', 'confirm_email', 'birth_date', 'bio', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        cleaned_email = cleaned_data.get('email')
        cleaned_verify = cleaned_data.get('confirm_email')

        # Check if email and confirm email match
        if cleaned_email != cleaned_verify:
            raise forms.ValidationError(
                "You need to enter the same email in both fields")

        # Check for duplicate emails, email must be unique to user
        try:
            models.Profile.objects.get(email__exact=cleaned_email)
        except models.Profile.MultipleObjectsReturned:
            raise forms.ValidationError(
                "Email Already Exists"
            )
        except models.Profile.DoesNotExist:
            pass


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = models.User

    # def clean(self):
    #     user = self.user
    #     cleaned_old_password = self.cleaned_data['old_password']
    #     new_password = self.cleaned_data['new_password1']
    #     if new_password == cleaned_old_password:
    #         raise forms.ValidationError(
    #             'Cannot use previous password'
    #         )
    #     first_name = user.first_name.lower()
    #     last_name = user.last_name.lower()
    #     username = user.username.lower()
    #
    #     if (first_name or last_name or username) in new_password.lower():
    #         raise forms.ValidationError(
    #             'Password cannot contain username, last name or first name'
    #         )
    #
    #     user.check_password(new_password)
