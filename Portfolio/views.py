from django.shortcuts import render,redirect
from accounts.models import Profile
from .forms import ContactForm
from django.contrib import messages
from .models import Project
from django.shortcuts import render, get_object_or_404

# Create your views here.

# - Homepage 

def home(request):
   
    profile = Profile.objects.first() 
    return render(request, 'Portfolio/Home.html', {'profile': profile})


def about_me(request):
    #Get the profile
    profile = Profile.objects.first() 

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Your message was sent successfully!")
            return redirect('about') 
    else:
        form = ContactForm()
    
    return render(request, 'Portfolio/about.html', {
        'profile': profile,
        'form': form
    })
 

def project_list(request):
    projects = Project.objects.all().order_by('-created_at') 
    return render(request, 'Portfolio/projects.html', {'projects': projects})

def project_detail(request, slug):
    # Fetch the project by its unique slug
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'Portfolio/project_detail.html', {'project': project})