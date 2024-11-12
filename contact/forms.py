from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=10)
    email=forms.EmailField()
    content=forms.CharField()
    