from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as mp
# Create your views here.



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'backend/dashboard.html')


@login_required(login_url='login')
def properties(request):
    return render(request, 'backend/properties.html')


@login_required(login_url='login')
def amenities(request):
    return render(request, 'backend/amenities.html')


@login_required(login_url='login')
def places(request):
    return render(request, 'backend/places.html')


@login_required(login_url='login')
def faq(request):
    return render(request, 'backend/faq.html')


@login_required(login_url='login')
def testimonials(request):
    return render(request, 'backend/testimonials.html')


@login_required(login_url='login')
def messages(request):
    return render(request, 'backend/messages.html')


@login_required(login_url='login')
def amenities_form(request):
    return render(request, 'backend/forms/amenities-form.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            mp.success(request, "Logged In")
            return redirect('dashboard') 
        else:
            mp.error(request, 'Invalid Credential')
            return render(request, 'backend/login.html')

    
    return render(request, 'backend/login.html')


# logout 
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    mp.success(request, "Sign Out")
    return redirect('login')



