from hashlib import new
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, ProfileForm, UserForm, CommentForm
from .models import Image, Profile, Like, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required(login_url='/accounts/login/')
def home(request):
    
    user = User.objects.get(username= request.user)
    profile = Profile.objects.all()
    posts = Image.all_posts().order_by('-pub_date')
    likes = Like.objects.all()
    users = User.objects.all()
    # delete_post = Image.delete_image(current_user)
   
    return render(request, 'home.html', {'current_user': user, "posts": posts, "profile": profile , "users":users})
@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get(username= request.user)
    profile = Profile.objects.all()
    posts = Image.objects.all()
    # posts = Image.objects.filter(profile__id=id)[::-1]
    return render(request, "profile.html", context={"user":user,"profile":profile, "posts": posts})


@login_required(login_url='/accounts/login/')          
def update_profile(request):
    current_user = request.user
    poster = Profile.objects.filter(user=request.user)
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
            
@login_required(login_url='/accounts/login/')
def like(request,operation,pk):
    post = get_object_or_404(Image,pk=pk)
    
    if operation == 'like':
        post.likes += 1
        post.save()
    elif operation =='unlike':
        post.likes -= 1
        post.save()
    return redirect('home')

@login_required(login_url='/accounts/login/')
def ShowUserPage(request, username):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.objects.get(user__username=search_term )
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"profiles": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
@login_required(login_url='/accounts/login/')        
def post_comment(request):
    postcomm = get_object_or_404(Image, )
    comments = postcomm.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(data =request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.postcomm = postcomm
            new_comment.save()
    else:
        form = CommentForm()                   
    return render(request, 'home.html', {"postcomm": postcomm, "comments": comments, "new_comment": new_comment, "comment_form": form})      
            
    
@login_required
def user_profile(request, username):
    user_prof = get_object_or_404(User, username=username)
    if request.user == user_prof:
        return redirect('profile', username=request.user.username)
    user_images = user_prof.profile.images.all()
   
    params = {
        'user_prof': user_prof,
        'user_images': user_images,
        
    }
  
    return render(request, 'users/user_profile.html', params)
    
    
    
    
# def profile(username):
#    user = User.query.filter_by(username=username).first() 
#    images = Images.query.filter_by(author = current_user.id).all()
#    return render_template("profile/profile.html", user = user, images= images)


# Create your views here.
