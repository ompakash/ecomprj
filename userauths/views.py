from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Hey {username}, Your account has been created successfully')
            new_user = authenticate(username = form.cleaned_data['email'], password = form.cleaned_data['password1'])
            login(request,new_user)
            print('user created')
            return redirect("core:index")
            
    else:
        print('User can not be register')
    context = {
        'form':form
    }

    return render(request,'userauths/sign-up.html',context)