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