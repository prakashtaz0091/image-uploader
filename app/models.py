from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.URLField()
    uploaded_image = models.ImageField(upload_to='uploaded_images/')
