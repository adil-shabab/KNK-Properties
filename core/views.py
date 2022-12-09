from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages as mp
from .forms import *
from .models import *
from django import template
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.text import slugify
import random



register = template.Library()
@register.filter()
def range(min=5):
    return range(min)

# Create your views here.





# api view 

class PlaceView(APIView):
    def get(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something Went Wrong"

        try:
            places = Places.objects.all()
            payload = []
            for place in places:
                payload.append({
                    'name': place.name
                })

            response['status'] = 200
            response['message'] = "All Places"
            response['data'] = payload

        except Exception as e:
            print(e)

        return Response(response)
    

    
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something Went Wrong"

        try:
            data = request.data
            print(data.get('name'))
            Places.objects.create(name=data.get('name'))
            response['status'] = 200
            response['message'] = "Place Added"

        except Exception as e:
            print(e)

        return Response(response)




PlaceView = PlaceView.as_view()




class MessageView(APIView):
    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = "Something Went Wrong"

        try:
            data = request.data
            Messages.objects.create(name=data.get('name'),message=data.get('message'),email=data.get('email'),number=data.get('number'))
            response['status'] = 200
            response['message'] = "Message Sent"

        except Exception as e:
            print(e)

        return Response(response)

MessageView = MessageView.as_view()










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
    faq = Faq.objects.all()
    count = Faq.objects.all().count()
    context = {
        'faq': faq,
        'count' : count
    }
    return render(request, 'backend/faq.html',context)


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
    messages = Messages.objects.all()
    messages_count = Messages.objects.all().count()
    context = {
        'messages' : messages,
        'count': messages_count
    }
    return render(request, 'backend/messages.html', context)




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





# create faq 
@login_required(login_url='login')
def faq_form(request):
    form = FaqForm()
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mp.success(request, 'Faq Added')
            return redirect('faq')
        else:
            return redirect('faq-form')

    context = {'form':form}
    return render(request, 'backend/forms/faq-form.html', context)


# update faq 
@login_required(login_url='login')
def faq_edit(request, pk):
    faq = Faq.objects.get(id=pk)
    form = FaqForm(instance=faq)
    if request.method == 'POST':
        form= FaqForm(request.POST, request.FILES, instance=faq)
        if form.is_valid():
            faq = form.save()
            mp.success(request, 'Faq Updated')
            return redirect('faq')
        else:
            return redirect('faq-edit')
    
    context = {'form':form, 'faq': faq}
    return render(request, 'backend/forms/faq-edit.html', context)


# delete faq 
@login_required(login_url='login')
def faq_delete(request,pk):
    faq = Faq.objects.get(id=pk)
    faq.delete()
    mp.success(request, 'Faq Deleted')
    return redirect('faq')




# delete message 
def message_delete(request,pk):
    msg = Messages.objects.get(id=pk)
    msg.delete()
    mp.success(request, 'Message Deleted')
    return redirect('messages')






# creation form 
@login_required(login_url='login')
def property_form(request):
    form = PropertyForm()
    places = Places.objects.all()
    if request.method == 'POST':
        form =PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            arr1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            arr2 = ['1','2','3','4','5','6','7','8','9','0']
            slug_name = form1.property_name + '-' + random.choice(arr1) + '-' + random.choice(arr2)
            slug = slugify(slug_name)
            form1.slug = slug
            form1.property_status = True


            # edited 
            # water_mark = media+'small-logo.png'

            # img1 = watermark_image(form1.property_image,form1.property_image,water_mark)

            # if form1.property_image_two:
            #     img2 = watermark_image(form1.property_image_two,form1.property_image_two,water_mark)
            #     form1.property_image_two = img2

            # if form1.property_image_three:
            #     img3 = watermark_image(form1.property_image_three,form1.property_image_three,water_mark)
            #     form1.property_image_three = img3

            # if form1.property_image_four:
            #     img4 = watermark_image(form1.property_image_four,form1.property_image_four,water_mark)
            #     form1.property_image_four = img4

            # if form1.property_image_five:
            #     img5 = watermark_image(form1.property_image_five,form1.property_image_five,water_mark)
            #     form1.property_image_five = img5

            # if form1.property_image_six:
            #     img6 = watermark_image(form1.property_image_six,form1.property_image_six,water_mark)
            #     form1.property_image_six = img6

            # if form1.property_image_seven:
            #     img7 = watermark_image(form1.property_image_seven,form1.property_image_seven,water_mark)
            #     form1.property_image_seven = img7

            # if form1.property_image_eight:
            #     img8 = watermark_image(form1.property_image_eight,form1.property_image_eight,water_mark)
            #     form1.property_image_eight = img8

            # if form1.property_image_nine:
            #     img9 = watermark_image(form1.property_image_nine,form1.property_image_nine,water_mark)
            #     form1.property_image_nine = img9

            # if form1.property_image_ten:
            #     img10 = watermark_image(form1.property_image_ten,form1.property_image_ten,water_mark)
            #     form1.property_image_ten = img10


            # form1.property_image = img1



            latest_property = Property.objects.order_by('-upload_date')[:1]
            print(latest_property)
            
            if len(latest_property) > 0:
                for x in latest_property:
                    reference_id = x.id + 1
                    start = 1000
                    ref_id = start + reference_id 
                    form1.ref_id = (f"{'KNK'}{ref_id}")
            else:
                start = 1000
                ref_id = start
                form1.ref_id = (f"{'KNK'}{ref_id}")


            form1.save()
            form1 = form.save()
            mp.success(request, "Property Added Successfully")
            return redirect('properties')
        else:
            return redirect('property-form')
            
    context = {'form':form,'places':places}
    return render(request, 'backend/forms/property-form.html', context)





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



