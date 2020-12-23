from django import forms
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45, min_length=2)
    last_name = forms.CharField(max_length=45, min_length=2)
    email = forms.CharField(max_length=45, min_length=2)
    password = forms.CharField(max_length=45, min_length=2, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=45, min_length=2, widget=forms.PasswordInput)
