from .models import Image
from django import forms

class NewPostForm(forms.Form):
    class Meta:
        model = Image
        exclude = ['pub_date', 'social_user']
        