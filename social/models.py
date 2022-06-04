from django.db import models
import datetime

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.image_name