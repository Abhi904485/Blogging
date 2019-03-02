from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFrom


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(username, first_name, last_name, email, password2, password1)
            messages.success(request, f'Yor Account with {username} Has been created for you are now able to log in. !')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        pu_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        up_form = UserUpdateForm(request.POST, instance=request.user)

        if pu_form.is_valid() and up_form.is_valid():
            pu_form.save()
            up_form.save()
            messages.success(request, f'Your Account Has been Updated ')
            return redirect('profile')
    else:
        pu_form = ProfileUpdateFrom(instance=request.user.profile)
        up_form = UserUpdateForm(instance=request.user)

    context = {
        "pu_form": pu_form,
        "up_form": up_form

    }
    return render(request, 'profile.html', context)
