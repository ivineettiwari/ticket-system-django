# forms.py
from django import forms

class AppForm(forms.Form):
    CHOICES = (
        ('', 'Select ticket type'),
        ('Access Request', 'Access Request'),
        ('Query', 'Query'),
        ('Defect', 'Defect'),
        ('Enhancement', 'Enhancement')
    )

    subject = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder': 'Enter your subject'}))
    discription = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Enter your discription', 'cols': 40, 'rows': 5}))
    ticket_type = forms.ChoiceField(choices=CHOICES, required=True, initial=None)
    comment = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your comment'}))
    active = forms.BooleanField()
    
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    