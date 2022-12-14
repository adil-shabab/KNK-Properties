from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('buy', views.buy, name='buy'),
    path('rent', views.rent, name='rent'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('premium', views.premium, name='premium'),
    path('international', views.international, name='international'),
    path('standard', views.standard, name='standard'),
    path('featured', views.featured, name='featured'),
    path('property/<slug:slug>', views.single, name='single'),
    path('listing/porperty', views.list, name='list'),
    path('property-management', views.property_management, name='property-management'),




    path('account/login', views.login, name='login'),
    path('account/logout', views.logout_user, name='logout'),
    path('account/', views.dashboard, name='dashboard'),
    path('account/properties', views.properties, name='properties'),
    path('account/amenities', views.amenities, name='amenities'),
    path('account/places', views.places, name='places'),

    path('account/faq', views.faq, name='faq'),
    path('account/testimonials', views.testimonials, name='testimonials'),
    path('account/messages', views.messages, name='messages'),

    
    path('account/subscriptions', views.subscriptions, name='subscriptions'),
    path('account/delete/subscription/<str:pk>', views.subscription_delete, name='subscription-delete'),



    path('account/ads/desktop', views.ads, name='ads'),
    path('account/ads/mobile', views.ads_mobile, name='ads_mobile'),
    path('account/innerad', views.inner_ad, name='inner_ad'),



    path('account/form/ads/master', views.master_ad_form, name='master_ad_form'),
    path('account/form/ads/master/<str:pk>', views.update_master_ad, name='update_master_ad'),
    path('account/ads/delete/master/<str:pk>', views.delete_master_ad, name='delete_master_ad'),

    path('account/ads/master/delete/image/two/<str:pk>', views.delete_two_of_master, name='delete_master_ad_two'),
    path('account/ads/master/delete/image/three/<str:pk>', views.delete_three_of_master, name='delete_master_ad_three'),


    path('account/form/ads/second', views.second_ad_form, name='second_ad_form'),
    path('account/form/ads/second/<str:pk>', views.update_second_ad, name='update_second_ad'),
    path('account/ads/delete/second/<str:pk>', views.delete_second_ad, name='delete_second_ad'),

    path('account/ads/second/delete/image/two/<str:pk>', views.delete_two_of_second, name='delete_second_ad_two'),
    path('account/ads/second/delete/image/three/<str:pk>', views.delete_three_of_second, name='delete_second_ad_three'),


    path('account/form/ads/third', views.third_ad_form, name='third_ad_form'),
    path('account/form/ads/third/<str:pk>', views.update_third_ad, name='update_third_ad'),
    path('account/ads/delete/third/<str:pk>', views.delete_third_ad, name='delete_third_ad'),
    
    path('account/ads/third/delete/image/two/<str:pk>', views.delete_two_of_third, name='delete_third_ad_two'),
    path('account/ads/third/delete/image/three/<str:pk>', views.delete_three_of_third, name='delete_third_ad_three'),






    # mobile ad 
    path('account/form/ads/mobile/master', views.master_ad_form_mobile, name='master_ad_form_mobile'),
    path('account/form/ads/mobile/master/<str:pk>', views.update_master_ad_mobile, name='update_master_ad_mobile'),
    path('account/ads/mobile/delete/master/<str:pk>', views.delete_master_ad_mobile, name='delete_master_ad_mobile'),

    path('account/ads/mobile/master/delete/image/two/<str:pk>', views.delete_two_of_master_mobile, name='delete_master_ad_two_mobile'),
    path('account/ads/mobile/master/delete/image/three/<str:pk>', views.delete_three_of_master_mobile, name='delete_master_ad_three_mobile'),


    path('account/form/ads/mobile/second', views.second_ad_form_mobile, name='second_ad_form_mobile'),
    path('account/form/ads/mobile/second/<str:pk>', views.update_second_ad_mobile, name='update_second_ad_mobile'),
    path('account/ads/delete/mobile/second/<str:pk>', views.delete_second_ad_mobile, name='delete_second_ad_mobile'),

    path('account/ads/mobile/second/delete/image/two/<str:pk>', views.delete_two_of_second_mobile, name='delete_second_ad_two_mobile'),
    path('account/ads/mobile/second/delete/image/three/<str:pk>', views.delete_three_of_second_mobile, name='delete_second_ad_three_mobile'),


    path('account/form/ads/mobile/third', views.third_ad_form_mobile, name='third_ad_form_mobile'),
    path('account/form/ads/mobile/third/<str:pk>', views.update_third_ad_mobile, name='update_third_ad_mobile'),
    path('account/ads/mobile/delete/third/<str:pk>', views.delete_third_ad_mobile, name='delete_third_ad_mobile'),
    
    path('account/ads/mobile/third/delete/image/two/<str:pk>', views.delete_two_of_third_mobile, name='delete_third_ad_two_mobile'),
    path('account/ads/mobile/third/delete/image/three/<str:pk>', views.delete_three_of_third_mobile, name='delete_third_ad_three_mobile'),




    path('account/form/ads/inner', views.inner_ad_form, name='inner_ad_form'),
    path('account/form/ads/inner/<str:pk>', views.update_inner_ad, name='update_inner_ad'),
    path('account/ads/delete/inner/<str:pk>', views.delete_inner_ad, name='delete_inner_ad'),

    path('account/ads/inner/delete/image/two/<str:pk>', views.delete_two_of_inner, name='delete_inner_ad_two'),
    path('account/ads/inner/delete/image/three/<str:pk>', views.delete_three_of_inner, name='delete_inner_ad_three'),








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
    path('account/suspend/property/<str:pk>', views.suspend_property, name='suspend_property'),
    path('account/enable/property/<str:pk>', views.enable_property, name='enable_property'),

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



    path('account/client/properties', views.client_properties, name='client_request'),
    path('account/client/properties/delete/<str:pk>', views.delete_client_property, name='delete_client_property'),
    path('account/client/properties/<str:pk>', views.single_client_property, name='single_client_property'),


    # api route 
    path('account/create/message', views.MessageView, name='create-message'),
    path('account/api/places', views.PlaceView, name='place-view'),
    path('account/create/subscription', views.SubscriptionView, name='create-subscription'),


    path('account/enable/faq/<str:pk>', views.enable_faq, name='enable_faq'),
    path('account/disable/faq/<str:pk>', views.disable_faq, name='disable_faq'),

    path('account/enable/testimonial/<str:pk>', views.enable_testimonial, name='enable_testimonial'),
    path('account/disable/testimonial/<str:pk>', views.disable_testimonial, name='disable_testimonial'),






    path('account/ads/suspend/one/master/<str:pk>', views.suspend_master_ad_one, name='suspend_master_ad_one'),
    path('account/ads/suspend/two/master/<str:pk>', views.suspend_master_ad_two, name='suspend_master_ad_two'),
    path('account/ads/suspend/three/master/<str:pk>', views.suspend_master_ad_three, name='suspend_master_ad_three'),

    path('account/ads/enable/one/master/<str:pk>', views.enable_master_ad_one, name='enable_master_ad_one'),
    path('account/ads/enable/two/master/<str:pk>', views.enable_master_ad_two, name='enable_master_ad_two'),
    path('account/ads/enable/three/master/<str:pk>', views.enable_master_ad_three, name='enable_master_ad_three'),



    path('account/ads/suspend/one/second/<str:pk>', views.suspend_second_ad_one, name='suspend_second_ad_one'),
    path('account/ads/suspend/two/second/<str:pk>', views.suspend_second_ad_two, name='suspend_second_ad_two'),
    path('account/ads/suspend/three/second/<str:pk>', views.suspend_second_ad_three, name='suspend_second_ad_three'),

    path('account/ads/enable/one/second/<str:pk>', views.enable_second_ad_one, name='enable_second_ad_one'),
    path('account/ads/enable/two/second/<str:pk>', views.enable_second_ad_two, name='enable_second_ad_two'),
    path('account/ads/enable/three/second/<str:pk>', views.enable_second_ad_three, name='enable_second_ad_three'),



    path('account/ads/suspend/one/third/<str:pk>', views.suspend_third_ad_one, name='suspend_third_ad_one'),
    path('account/ads/suspend/two/third/<str:pk>', views.suspend_third_ad_two, name='suspend_third_ad_two'),
    path('account/ads/suspend/three/third/<str:pk>', views.suspend_third_ad_three, name='suspend_third_ad_three'),

    path('account/ads/enable/one/third/<str:pk>', views.enable_third_ad_one, name='enable_third_ad_one'),
    path('account/ads/enable/two/third/<str:pk>', views.enable_third_ad_two, name='enable_third_ad_two'),
    path('account/ads/enable/three/third/<str:pk>', views.enable_third_ad_three, name='enable_third_ad_three'),










    path('account/ads/mobile/suspend/one/master/<str:pk>', views.suspend_mobile_master_ad_one, name='suspend_mobile_master_ad_one'),
    path('account/ads/mobile/suspend/two/master/<str:pk>', views.suspend_mobile_master_ad_two, name='suspend_mobile_master_ad_two'),
    path('account/ads/mobile/suspend/three/master/<str:pk>', views.suspend_mobile_master_ad_three, name='suspend_mobile_master_ad_three'),

    path('account/ads/mobile/enable/one/master/<str:pk>', views.enable_mobile_master_ad_one, name='enable_mobile_master_ad_one'),
    path('account/ads/mobile/enable/two/master/<str:pk>', views.enable_mobile_master_ad_two, name='enable_mobile_master_ad_two'),
    path('account/ads/mobile/enable/three/master/<str:pk>', views.enable_mobile_master_ad_three, name='enable_mobile_master_ad_three'),



    path('account/ads/mobile/suspend/one/second/<str:pk>', views.suspend_mobile_second_ad_one, name='suspend_mobile_second_ad_one'),
    path('account/ads/mobile/suspend/two/second/<str:pk>', views.suspend_mobile_second_ad_two, name='suspend_mobile_second_ad_two'),
    path('account/ads/mobile/suspend/three/second/<str:pk>', views.suspend_mobile_second_ad_three, name='suspend_mobile_second_ad_three'),

    path('account/ads/mobile/enable/one/second/<str:pk>', views.enable_mobile_second_ad_one, name='enable_mobile_second_ad_one'),
    path('account/ads/mobile/enable/two/second/<str:pk>', views.enable_mobile_second_ad_two, name='enable_mobile_second_ad_two'),
    path('account/ads/mobile/enable/three/second/<str:pk>', views.enable_mobile_second_ad_three, name='enable_mobile_second_ad_three'),



    path('account/ads/mobile/suspend/one/third/<str:pk>', views.suspend_mobile_third_ad_one, name='suspend_mobile_third_ad_one'),
    path('account/ads/mobile/suspend/two/third/<str:pk>', views.suspend_mobile_third_ad_two, name='suspend_mobile_third_ad_two'),
    path('account/ads/mobile/suspend/three/third/<str:pk>', views.suspend_mobile_third_ad_three, name='suspend_mobile_third_ad_three'),

    path('account/ads/mobile/enable/one/third/<str:pk>', views.enable_mobile_third_ad_one, name='enable_mobile_third_ad_one'),
    path('account/ads/mobile/enable/two/third/<str:pk>', views.enable_mobile_third_ad_two, name='enable_mobile_third_ad_two'),
    path('account/ads/mobile/enable/three/third/<str:pk>', views.enable_mobile_third_ad_three, name='enable_mobile_third_ad_three'),




    path('account/ads/inner/suspend/one/third/<str:pk>', views.suspend_inner_ad_one, name='suspend_inner_ad_one'),
    path('account/ads/inner/suspend/two/third/<str:pk>', views.suspend_inner_ad_two, name='suspend_inner_ad_two'),
    path('account/ads/inner/suspend/three/third/<str:pk>', views.suspend_inner_ad_three, name='suspend_inner_ad_three'),

    path('account/ads/inner/enable/one/third/<str:pk>', views.enable_inner_ad_one, name='enable_inner_ad_one'),
    path('account/ads/inner/enable/two/third/<str:pk>', views.enable_inner_ad_two, name='enable_inner_ad_two'),
    path('account/ads/inner/enable/three/third/<str:pk>', views.enable_inner_ad_three, name='enable_inner_ad_three'),

]