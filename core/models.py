from django.db import models
from tinymce.models import HTMLField


# Create your models here.


class Amenities(models.Model):
    amenities_name = models.CharField(max_length=150)
    amenities_icon = models.ImageField(upload_to='media')

    def __str__(self):
        return self.amenities_name



class Places(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name



class Testimonial(models.Model):
    photo = models.ImageField(upload_to='media')
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    review = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.name




class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()





class Messages(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    number = models.CharField(max_length=250,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    message = models.TextField()


    def __str__ (self):
        return self.name






class Property(models.Model):
    property_name = models.CharField(max_length=300)
    property_location = models.CharField(max_length=150)
    property_type = models.CharField(max_length=150, default='Villa')
    buy_rent = models.CharField(max_length=150, default='Buy')
    total_bedroom = models.IntegerField()
    total_bathroom = models.IntegerField()
    property_price = models.IntegerField()
    property_listing = models.CharField(max_length=150, default='Standard Listing',null=True, blank=True)
    property_area = models.IntegerField()
    property_keyword = models.TextField(null=True, blank=True)
    # is_commercial_property = models.BooleanField(default=False)
    property_description = HTMLField(null=True, blank=True)
    property_video_link = models.CharField(max_length=200, null=True, blank=True)
    is_international_property = models.BooleanField(default=False)
    property_image = models.ImageField(upload_to='media')
    property_image_two = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_three = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_four = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_five = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_six = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_seven = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_eight = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_nine = models.ImageField(upload_to='media', null=True, blank=True)
    property_image_ten = models.ImageField(upload_to='media', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True, null=True)
    property_map_location = models.CharField(max_length=150, null=True, blank=True)
    property_amenities = models.ManyToManyField('Amenities')
    slug = models.TextField(null=True, blank=True, unique=True)
    property_status =  models.BooleanField(default=True)
    water_and_electricity = models.CharField(max_length=150, default='Exclusive')
    parking_slot = models.IntegerField(null=True, blank=True)
    furnished_type = models.CharField(max_length=150, default='Furnished')



    is_premium = models.BooleanField(default=False)
    is_standard = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)


    meta_title = models.CharField(max_length=150, null=True, blank=True)
    meta_keyword = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    ref_id = models.CharField(max_length=200,null=True, blank=True)


    def __str__(self):
        return self.property_name





class MasterAd(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)




class SecondAd(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)




class ThirdAd(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)




class InnerAd(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)







class MasterAdMobile(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)




class SecondAdMobile(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)




class ThirdAdMobile(models.Model):
    ad_one = models.ImageField(upload_to = 'media')
    ad_two = models.ImageField(upload_to='media', null=True, blank=True)
    ad_three = models.ImageField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=True)
    ad_one_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_two_link =  models.CharField(null=True, blank=True, max_length=200)
    ad_three_link =  models.CharField(null=True, blank=True, max_length=200)


