from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, TextInput, ImageField, IntegerField
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




Type = [
    ('Apartment', 'Apartment'),
    ('Short Term & Hotel', 'Short Term & Hotel'),
    ('Villa', 'Villa'),
    ('Commercial Spaces ', 'Commercial Spaces '),
    ('Hotel Apartment', 'Hotel Apartment'),
    ('Staff Accommodation ', 'Staff Accommodation '),
    ('Duplex', 'Duplex'),
    ('Whole building', 'Whole building'),
]

BuyOrRent = [
   ('Rent', 'Rent'),
   ('Buy', 'Buy')
]
List = [
    ('Premium Listing', 'Premium Listing'),
    ('Standard Listing', 'Standard Listing'),
    ('Featured Listing', 'Featured Listing'),
]
Water = [
    ('Inclusive', 'Inclusive'),
    ('Exclusive', 'Exclusive')
]
Furnished = [
    ('Furnished', 'Furnished'),
    ('Semi Furnished', 'Semi Furnished'),
    ('Unfurnished', 'Unfurnished')
]







class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

        widgets = {
            'property_type' : forms.Select(choices=Type),
            'furnished_type' : forms.Select(choices=Furnished),
            'water_and_electricity' : forms.Select(choices=Water),
            'buy_rent' : forms.RadioSelect(choices=BuyOrRent, attrs={'class': 'mt-2'}),
            'property_listing' : forms.RadioSelect(choices=List, attrs={'class':'mt-2'}),
            'property_amenities' : forms.CheckboxSelectMultiple(attrs={'class': 'mt-2'}),
            'property_image' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_two' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_three' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_four' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_five' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_six' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_seven' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_eight' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_nine' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_ten' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
        }







class AmenitiesForm(ModelForm):
    class Meta:
        model = Amenities
        fields = ['amenities_name', 'amenities_icon']

        widgets = {
            'amenities_name' : forms.TextInput(attrs={'class': 'input'}),
            'amenities_icon' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }



class PlaceForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'



class TestimonialForm(ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

        widgets = {
            'photo' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'name' : forms.TextInput(),
            'designation' : forms.TextInput(),
            'review' : forms.Textarea(),
        }




class FaqForm(ModelForm):
    class Meta:
        model = Faq
        fields = '__all__'

        widgets = {
            'question' : forms.TextInput(),
            'answer' : forms.Textarea()
        }




class MessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'








class MasterAdForm(ModelForm):
    class Meta:
        model = MasterAd
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }


class SecondAdForm(ModelForm):
    class Meta:
        model = SecondAd
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }


class ThirdAdForm(ModelForm):
    class Meta:
        model = ThirdAd
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }


class InnerAdForm(ModelForm):
    class Meta:
        model = InnerAd
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }




class MasterAdFormMobile(ModelForm):
    class Meta:
        model = MasterAdMobile
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }


class SecondAdFormMobile(ModelForm):
    class Meta:
        model = SecondAdMobile
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }


class ThirdAdFormMobile(ModelForm):
    class Meta:
        model = ThirdAdMobile
        fields = '__all__'

        widgets = {
            'ad_one' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_two' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
            'ad_three' : forms.FileInput(attrs={'class': 'image-field image-upload', 'accept': "image/*"}),
        }


    

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

        widgets = {
            'property_type' : forms.Select(choices=Type),
            'furnished_type' : forms.Select(choices=Furnished),
            'buy_rent' : forms.RadioSelect(choices=BuyOrRent, attrs={'class': 'mt-2'}),
            'property_image' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_two' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
            'property_image_three' : forms.FileInput(attrs={'class': 'image-field image-upload'}),
        }
