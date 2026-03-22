from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=15, blank=True)
    
    
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Profile(models.Model):
    # Link to your Custom User
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    
    # Basic Info
    full_name = models.CharField(max_length=100, blank=True)
    headline = models.CharField(max_length=200, help_text="e.g. Full Stack Developer ", blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg', blank=True)
    location = models.CharField(max_length=100, blank=True)
    
    # Contact & Socials
    phone_number = models.CharField(max_length=20, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True, help_text="Personal blog or external site")
    
    # Professional Details
    cv_file = models.FileField(upload_to='cvs/', blank=True, help_text="Upload your PDF resume")
    skills = models.TextField(help_text="Enter skills separated by commas (e.g. Python, Django, React)", blank=True)
    is_available_for_hire = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Portfolio Profile"

    # Helper method to turn skills string into a list for templates
    def get_skills_list(self):
        return [skill.strip() for skill in self.skills.split(',')] if self.skills else []