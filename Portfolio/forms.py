from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
       
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'email@example.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 4, 'placeholder': 'How can I help?'}),
        }
