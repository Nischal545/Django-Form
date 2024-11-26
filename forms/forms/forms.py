from django import forms

class InputForm(forms.Form):
    firstName = forms.CharField(max_length=200)
    lastName = forms.CharField(max_length=200)
    rollNum = forms.IntegerField(help_text="Enter 6 digit roll number")
    password = forms.CharField(widget=forms.PasswordInput())
