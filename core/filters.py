
import django_filters
from .models import *
from django import forms
from django.forms.widgets import TextInput,RadioSelect

# from django import forms


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

Buy = [
    ('Rent','Rent'),
    ('Buy','Buy'),
    # ('Buy and Rent','Buy and Rent'),
]





class PropertyFilter(django_filters.FilterSet):
    buy_rent = django_filters.ChoiceFilter(lookup_expr='icontains', choices=Buy)
    property_name = django_filters.CharFilter(widget=TextInput(attrs={'class':'input','placeholder': 'Search Properties'}), lookup_expr='icontains')
    property_keyword = django_filters.CharFilter(widget=TextInput(attrs={'class':'input','placeholder': 'Search Keyword'}), lookup_expr='icontains')
    property_location = django_filters.CharFilter(widget=TextInput(attrs={'class':'input','placeholder': 'Search Location'}), lookup_expr='icontains')
    ref_id = django_filters.CharFilter(widget=TextInput(attrs={'class':'input','placeholder': 'Ref Id'}), lookup_expr='icontains')
    property_type = django_filters.ChoiceFilter(lookup_expr='icontains',choices=Type)
    
    min_count_bedroom = django_filters.NumberFilter(field_name='total_bedroom', lookup_expr='gte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Min Bedroom'}))
    max_count_bedroom = django_filters.NumberFilter(field_name='total_bedroom', lookup_expr='lte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Max Bedroom'}))

    min_count_area = django_filters.NumberFilter(field_name='property_area', lookup_expr='gte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Min Area'}))
    max_count_area = django_filters.NumberFilter(field_name='property_area', lookup_expr='lte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Max Area'}))

    min_count_bathroom = django_filters.NumberFilter(field_name='total_bathroom', lookup_expr='gte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Min Bathroom'}))
    max_count_bathroom = django_filters.NumberFilter(field_name='total_bathroom', lookup_expr='lte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Max Bathroom'}))

    min_price = django_filters.NumberFilter(field_name='property_price', lookup_expr='gte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Min Price'}))
    max_price = django_filters.NumberFilter(field_name='property_price', lookup_expr='lte', widget=TextInput(attrs={'class':'input', 'placeholder': 'Max Price'}))


    widgets = {
            'buy_rent' : forms.RadioSelect(choices=Buy, attrs={'class': 'mt-2'}),
        }

    class Meta:
        model = Property
        fields = [  
                    'buy_rent',
                    'property_location',
                    'property_name', 
                    'property_type', 
                    'total_bathroom' , 
                    'total_bedroom'
                ]
        exclude = [
            'total_bathroom',
            'total_bedroom'
        ]