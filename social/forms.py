from .models import Image, Profile, Comment
from django import forms
from django.contrib.auth.models import User
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'social_user', 'user_profile']
        
class UserForm(forms.ModelForm):
    class Meta: 
        model = User
        
        fields = ['email', 'username']


class ProfileForm(forms.ModelForm):
    class Meta: 
        model = Profile
        
        fields = ['bio', 'profile_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['comment']
        