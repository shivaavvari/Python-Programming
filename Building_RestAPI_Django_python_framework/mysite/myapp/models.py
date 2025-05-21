from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.name
    images = models.ImageField(upload_to = 'Images',default="Images/None/sampleImg.jpg")
    name = models.CharField(max_length=100)
    description= models.CharField(max_length=200)
    ratings = models.FloatField()
