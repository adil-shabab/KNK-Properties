from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('buy/', views.buy, name='buy'),
    path('rent/', views.rent, name='rent'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('premium/', views.premium, name='premium'),
    path('standard/', views.standard, name='standard'),
    path('featured/', views.featured, name='featured'),




    path('account/login', views.login, name='login'),
    path('account/logout', views.logout_user, name='logout'),
    path('account/', views.dashboard, name='dashboard'),
    path('account/properties', views.properties, name='properties'),
    path('account/amenities', views.amenities, name='amenities'),
    path('account/places', views.places, name='places'),

    path('account/faq', views.faq, name='faq'),
    path('account/testimonials', views.testimonials, name='testimonials'),
    path('account/messages', views.messages, name='messages'),


    path('account/form/amenities', views.amenities_form, name='amenities-form'),
    path('account/form/amenities/<str:pk>', views.amenities_edit, name='amenities-edit'),
    path('account/delete/amenities/<str:pk>', views.amenities_delete, name='amenities-delete'),

    path('account/form/places', views.place_form, name='place-form'),
    path('account/form/places/<str:pk>', views.place_edit, name='place-edit'),
    path('account/delete/places/<str:pk>', views.place_delete, name='place-delete'),

    path('account/form/testimonials', views.testimonial_form, name='testimonial-form'),
    path('account/form/testimonials/<str:pk>', views.testimonial_edit, name='testimonial-edit'),
    path('account/delete/testimonials/<str:pk>', views.testimonial_delete, name='testimonial-delete'),

    path('account/form/faq', views.faq_form, name='faq-form'),
    path('account/form/faq/<str:pk>', views.faq_edit, name='faq-edit'),
    path('account/delete/faq/<str:pk>', views.faq_delete, name='faq-delete'),

    path('account/form/property', views.property_form, name='property-form'),
    path('account/form/property/<str:pk>', views.property_edit, name='property-edit'),
    path('account/delete/property/<str:pk>', views.property_delete, name='property-delete'),

    path('account/delete/messages/<str:pk>', views.message_delete, name='message-delete'),


    path('account/property/delete/image/two/<str:pk>', views.delete_two_of_ten, name='delete_two_of_ten'),
    path('account/property/delete/image/three/<str:pk>', views.delete_three_of_ten, name='delete_three_of_ten'),
    path('account/property/delete/image/four/<str:pk>', views.delete_four_of_ten, name='delete_four_of_ten'),
    path('account/property/delete/image/five/<str:pk>', views.delete_five_of_ten, name='delete_five_of_ten'),
    path('account/property/delete/image/six/<str:pk>', views.delete_six_of_ten, name='delete_six_of_ten'),
    path('account/property/delete/image/seven/<str:pk>', views.delete_seven_of_ten, name='delete_seven_of_ten'),
    path('account/property/delete/image/eight/<str:pk>', views.delete_eight_of_ten, name='delete_eight_of_ten'),
    path('account/property/delete/image/nine/<str:pk>', views.delete_nine_of_ten, name='delete_nine_of_ten'),
    path('account/property/delete/image/ten/<str:pk>', views.delete_ten_of_ten, name='delete_ten_of_ten'),



    # api route 
    path('account/create/message', views.MessageView, name='create-message'),
    path('account/api/places', views.PlaceView, name='place-view'),
]