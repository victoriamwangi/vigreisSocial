from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ProfileForm
from .models import Image

def home(request):
    current_user = request.user
    posts = Image.all_posts().order_by('-pub_date')
    # delete_post = Image.delete_image(current_user)
    return render(request, 'home.html', {'current_user': current_user, "posts": posts, })

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.social_user = current_user
            post.user_profile = current_user
            post.save()
        return redirect('home')
    else: 
        form = NewPostForm()
        return render(request, 'new_post.html', {'form': form})
def profile(request):
    current_user = request.user
    posts = Image.all_posts().order_by('-pub_date')   
    if request.method == 'POST':
        form= ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            post.save()
        return redirect('home')
        
    else:
        form = ProfileForm()
        return render(request, 'profile.html', {'current_user': current_user, "posts": posts, "form": form})
            


# Create your views here.
