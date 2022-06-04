from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm

def home(request):
    current_user = request.user
    return render(request, 'home.html', {'current_user': current_user})
@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.social_user = current_user
            post.save()
        return redirect('home')
    else: 
        form = NewPostForm()
        return render(request, 'new_post.html', {'form': form})

            


# Create your views here.
