from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,Profile

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=CustomUser

    list_display=['email','username','phone_number']





@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'is_staff')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'headline', 'is_available_for_hire')
    # This makes the admin look professional
    fieldsets = (
        ('Personal Info', {'fields': ('user', 'full_name', 'headline', 'bio', 'profile_pic')}),
        ('Socials', {'fields': ('github_url', 'linkedin_url', 'website_url')}),
        ('Professional', {'fields': ('cv_file', 'skills', 'is_available_for_hire')}),
    )
