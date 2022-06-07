from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ProfileForm, UserForm
from .models import Image, Profile, Like
from django.contrib.auth.models import User


def home(request):
    
    user = User.objects.get(username= request.user)
    profile = Profile.objects.all()
    posts = Image.all_posts().order_by('-pub_date')
    likes = Like.objects.all()
    # delete_post = Image.delete_image(current_user)
    return render(request, 'home.html', {'current_user': user, "posts": posts, "profile": profile })

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

@login_required
def profile(request):
    user = User.objects.get(username= request.user)
    profile = Profile.objects.all()
    posts = Image.objects.all()
    # posts = Image.objects.filter(profile__id=id)[::-1]
    return render(request, "profile.html", context={"user":user,"profile":profile, "posts": posts})

# def profile(request):
#     current_user = request.user
#     poster = Profile.objects.filter(username=request.user)
#     # poster = Profile.objects.filter(username= current_user)
    
#     return render(request, 'profile.html', {'current_user': current_user, "poster": poster})
            
def update_profile(request):
    current_user = request.user
    poster = Profile.objects.filter(username=request.user)
    # poster = Profile.objects.filter(username= current_user)
    posts = Image.all_posts().order_by('-pub_date')   
    if request.method == 'POST':
        form= ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit= False)
            form.instance.username.id = User.objects.get(username=request.user.id)
            post.save()
        return redirect('profile')
        
    else:
        form = ProfileForm()
        return render(request, 'update_profile.html', {'current_user': current_user, "posts": posts, "form": form, "poster": poster})
            
    
    
    
    
    
    
# def profile(username):
#    user = User.query.filter_by(username=username).first() 
#    images = Images.query.filter_by(author = current_user.id).all()
#    return render_template("profile/profile.html", user = user, images= images)


# Create your views here.
