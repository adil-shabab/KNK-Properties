from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as mp
from .forms import *
from .models import *
# Create your views here.



@login_required(login_url='login')
def dashboard(request):
    return render(request, 'backend/dashboard.html')


@login_required(login_url='login')
def properties(request):
    return render(request, 'backend/properties.html')


@login_required(login_url='login')
def amenities(request):
    amenities = Amenities.objects.all()
    amenities_count = Amenities.objects.all().count
    context = {
        'amenities': amenities,
        'amenities_count': amenities_count
    }
    return render(request, 'backend/amenities.html', context=context)


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




# forms  
# 
#  
# amenities creation form 
@login_required(login_url='login')
def amenities_form(request):
    form = AmenitiesForm()
    if request.method == 'POST':
        form = AmenitiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mp.success(request,  "Amenities Added")
            return redirect('amenities')
        else:
            return redirect('amenities-form')

    context = {'form':form}
    return render(request, 'backend/forms/amenities-form.html', context)



# update amenities 
@login_required(login_url='login')
def amenities_edit(request, pk):
    amenities = Amenities.objects.get(id=pk)
    form = AmenitiesForm(instance=amenities)
    if request.method == 'POST':
        form = AmenitiesForm(request.POST, request.FILES, instance=amenities)
        if form.is_valid():
            amenities = form.save()
            mp.success(request, amenities.amenities_name + ' ' + "Updated Successfully")
            return redirect('amenities')
        else:
            return redirect('amenities-edit')
    
    context = {'form':form, 'amenities': amenities}
    return render(request, 'backend/forms/amenities-edit.html', context)



# delete amenities 
@login_required(login_url='login')
def amenities_delete(request,pk):
    amenities = Amenities.objects.get(id=pk)
    amenities.delete()
    mp.success(request, amenities.amenities_name + ' ' + "deleted Successfully")
    return redirect('amenities')








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



