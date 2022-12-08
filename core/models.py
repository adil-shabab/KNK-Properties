from django.db import models

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

