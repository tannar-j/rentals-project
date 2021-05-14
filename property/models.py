from django.db import models

class Property(models.Model):
    image1 = models.ImageField(upload_to = 'images/')
    image2 = models.ImageField(upload_to = 'images/', default = '')
    image3 = models.ImageField(upload_to = 'images/', default = '')
    image4 = models.ImageField(upload_to = 'images/', default = '')
    curbside = models.ImageField(upload_to = 'images/', default = '')
    address = models.CharField(max_length=200, default = 'Set Address')
    summary = models.CharField(max_length=200)
    price = models.CharField(max_length = 10)
    area = models.CharField(max_length = 10, default = '0')
    bedrooms = models.CharField(max_length = 10, default = '0')
    baths = models.CharField(max_length = 10, default = '0')
