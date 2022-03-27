from cProfile import label
from email.policy import default
from django import forms

diet_choices = (
    ("Vegetarian", "Vegetarian"),
    ("Vegan", "Vegan"),
    ("Pescatarians", "Pescatarians"),
    ("Normal (Hybrid)", "Normal (Hybrid)"),
    ("Keto", "Keto"),
)

sex_choices = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class UserCreation(forms.Form):
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Email'}))
    username = forms.CharField(label=False, min_length=3, max_length=20, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Username'}))
    password = forms.CharField(label=False, min_length=6, max_length=20, widget=forms.TextInput(attrs={'class':'su-field', 'placeholder':'Password (6 Characters Minimum)', 'type':'password'}))
    height = forms.IntegerField(label=False)
    weight = forms.IntegerField(label=False)
    age = forms.IntegerField(label=False)
    sex = forms.ChoiceField(choices=sex_choices)
    diet = forms.ChoiceField(choices=diet_choices)
    excercise = forms.IntegerField(label=False) # Times per week


