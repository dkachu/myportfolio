from django.urls import path
from . import views


urlpatterns = [
    #  Homepage
    path('', views.home, name='home'),
    
    # Path for the About Me page (includes the contact form)
    path('about/', views.about_me, name='about'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),

]
