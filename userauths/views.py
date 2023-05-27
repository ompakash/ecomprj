from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserRegisterForm
from django.contrib import messages
from userauths.models import User
from django.conf import settings

# User = settings.AUTH_USER_MODEL

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


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,'Hey you are already Logged In')
        return redirect("core:index")

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"You are logged in.")
                return redirect('core:index')
            else:
                messages.warning(request,'User does not Exist, Create an account.')
        except:
            messages.warning(request,f'user with {email} does not exist')
        
        
    
    context = {

    }

    return render(request,'userauths/sign-in.html',context)








def logout_view(request):
    logout(request)
    messages.success(request,"You logged out")
    return redirect('userauths:sign-in')