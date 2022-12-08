from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields, TextInput, ImageField, IntegerField
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





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