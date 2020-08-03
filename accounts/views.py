from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm


def register(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,'Your account has been Created! Login in to access your account')
			return redirect('login')
		else:
			messages.success(request,'Your account cannot be Created! Please input correct data.')
			return render(request,'register.html',{'form':form})

	else:
		form = UserRegisterForm()
		return render(request,'register.html',{'form':form})
