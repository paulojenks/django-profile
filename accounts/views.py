from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from . import models
from . import forms


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('home')  # TODO: go to profile
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            profile = models.Profile(user=request.user)
            profile.save()
            return HttpResponseRedirect(reverse('accounts:profile'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile_view(request):
    '''User Profile View'''
    profile = get_object_or_404(models.Profile, id=request.user.id)
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    '''View to display the edit form.'''
    user = get_object_or_404(models.Profile, user=request.user)
    profile_form = forms.ProfileForm(instance=user)
    if request.method == 'POST':
        profile_form = forms.ProfileForm(instance=user, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form})


@login_required
def change_password(request):
    '''View to display the form for changing passwords.'''
    form = forms.CustomPasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = forms.CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was updated!')
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/change_password.html', {'form': form})
