from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as mp
from .forms import *
from .models import *
from django import template


register = template.Library()
@register.filter()
def range(min=5):
    return range(min)

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
    places = Places.objects.all()
    places_count = Places.objects.all().count
    context = {
        'places': places,
        'places_count': places_count
    }
    return render(request, 'backend/places.html', context)


@login_required(login_url='login')
def faq(request):
    return render(request, 'backend/faq.html')


@login_required(login_url='login')
def testimonials(request):
    testimonials = Testimonial.objects.all()
    count = Testimonial.objects.all().count()
    context={
        'testimonials':testimonials,
        'count': count
    }
    return render(request, 'backend/testimonials.html', context)


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









# place form 
# create place 
@login_required(login_url='login')
def place_form(request):
    form = PlaceForm()
    places = Places.objects.all()
    if request.method == 'POST':
        form =PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mp.success(request,  "Place Added Successfully")
            return redirect('places')
        else:
            return redirect('place-form')

    context = {'form':form}
    return render(request, 'backend/forms/places-form.html', context)



# update place 
@login_required(login_url='login')
def place_edit(request, pk):
    place = Places.objects.get(id=pk)

    form = PlaceForm(instance=place)
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            mp.success(request, place.name + ' ' + "Updated Successfully")
            return redirect('places')
        else:
            return redirect('place-edit')
    context = {'form':form}
    return render(request, 'backend/forms/places-edit.html', context)


# delete place 
@login_required(login_url='login')
def place_delete(request, pk):
    place = Places.objects.get(id=pk)
    place.delete()
    mp.success(request, place.name + ' ' + "deleted Successfully")
    return redirect('places')




# create testimonial 
@login_required(login_url='login')
def testimonial_form(request):
    form = TestimonialForm()
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mp.success(request, 'Testimonial Created')
            return redirect('testimonials')
        else:
            return redirect('testimonialform')

    context = {'form':form}
    return render(request, 'backend/forms/testimonials-form.html', context)


# update testimonial 
@login_required(login_url='login')
def testimonial_edit(request, pk):
    testimonial = Testimonial.objects.get(id=pk)
    form = TestimonialForm(instance=testimonial)
    if request.method == 'POST':
        form= TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            mp.success(request, 'Testimonial Updated')
            return redirect('testimonials')
    
    context = {'form':form, 'testimonial': testimonial}
    return render(request, 'backend/forms/testimonials-edit.html', context)



# delete testimonial 
@login_required(login_url='login')
def testimonial_delete(request,pk):
    testimonial = Testimonial.objects.get(id=pk)
    testimonial.delete()
    mp.success(request, 'Testimonial Deleted')
    return redirect('testimonials')











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



