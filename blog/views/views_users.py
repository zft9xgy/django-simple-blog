from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# user login and logout 
def userLogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            next = request.GET.get('next')
            return redirect(next or 'home')

    return render(request,'users/login.html')


@login_required(login_url='user-login')
def userLogout(request):
    
    logout(request)
    return redirect('home')