from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from . import forms
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your views here.
def sign_up(request):
    registered=False
    form=forms.SignUpForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            registered=True
    dict={
        'form':form,
        'registered':registered,
    }
    
    return render (request,'app_login/signup.html',context=dict)


def user_login(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect (reverse('index'))
    dict={
        'form':form
    }
    return render(request,'app_login/login.html',context=dict)

@login_required 
def logout_user(request):
    logout(request)
    return redirect('index')

@login_required 
def profile(request):
    return render(request,'app_login/profile.html',context={})


@login_required
def user_change(request):
    current_user = request.user
    changed=False
    if request.method == "POST":
        form = forms.UserChangeForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = forms.UserChangeForm(instance=current_user)  # Reinitialize the form
            changed=True
            return render(request, "app_login/profile.html", context={'form': form,'changed':changed,"value":'Profile',})
    else:
        form = forms.UserChangeForm(instance=current_user)
    
    return render(request, 'app_login/change_profile.html', context={'form': form,'changed':changed})


@login_required
def pass_change(request):
    current_user=request.user
    changed=False
    form=forms.PasswordChangeForm(current_user)
    if request.method =="POST":
        form=forms.PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            changed=True
        return render(request,"app_login/profile.html",context={'form':form,'changed':changed,"value":'Password',}) 
    return render(request,'app_login/change_pass.html',context={'form':form,'changed':changed})  



@login_required
def add_pro_pic(request):
        form=forms.ProfilePic()
        if request.method=="POST":
            form=forms.ProfilePic(request.POST,request.FILES)
            if form.is_valid():
                img=form.save(commit=False)
                img.user=request.user
                img.save()
                return HttpResponseRedirect(reverse('app_login:profile'))
        return render(request,'app_login/add_pro_pic.html',context={'form':form})
    
@login_required
def change_pro_pic(request):
    form=forms.ProfilePic(instance=request.user.user_profile)
    if request.method=="POST":
            form=forms.ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
            if form.is_valid():
                img=form.save(commit=False)
                img.user=request.user
                img.save()
                return HttpResponseRedirect(reverse('app_login:profile'))
    
    return render(request,'app_login/add_pro_pic.html',context={'form':form})
        