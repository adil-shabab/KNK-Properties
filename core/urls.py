from django.urls import path
from . import views

urlpatterns = [
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
]
