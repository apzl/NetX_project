
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import  CreateUserForm, UpdateUserForm, UpdateProfileForm
import random

def registerPage(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
		    form.save()
		    user = form.cleaned_data.get('username')
		    messages.success(request, 'Account was created for ' + user)
		    return redirect('login')
		else:
			form=CreateUserForm()		
			context = {'form':form}
			return render(request, 'signup.html', context)

		
	else:
		form=CreateUserForm()		
		context = {'form':form}
		return render(request, 'signup.html', context)

@login_required
def profilePage(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

@login_required
def matchPage(request):
    userg = request.user.profile.gender
    
