from .models import Image, Profile
from django import forms

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'social_user', 'user_profile']
        
class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        
        