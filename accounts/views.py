from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

@csrf_exempt #This skips csrf validation. Use csrf_protect to have validation
# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1']== request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'username already taken'})
            except:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            print("error")
            return render(request, 'accounts/signup.html',{'error':'password doesn\'t match'})
    else:
        #adjd

        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password incorrect'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
