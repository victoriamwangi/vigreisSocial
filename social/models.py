from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.

# class User(models.Model):
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    social_user = models.ForeignKey(User, on_delete= models.CASCADE)
    user_profile = models.ForeignKey('Profile', on_delete= models.CASCADE)
    image_caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/', null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    
    @classmethod
    def all_posts(cls):
        posts = Image.objects.all()
        return posts
    def __str__(self):
        return self.image_name
    
class Profile(models.Model):
    # user_name = models.ForeignKey("User", on_delete= models.CASCADE)
    email = models.CharField(max_length= 30)
    bio = models.CharField(max_length= 50)
    profile_image = models.ImageField(upload_to = 'images/', null=True, blank= True)
    location= models.CharField(max_length=20)
   
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
         
        
   

    def __str__(self):
        return self.user_name