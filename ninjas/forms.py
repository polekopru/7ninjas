from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Name', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    last_name = forms.CharField(max_length=30, label='Surname', widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    captcha = NoReCaptchaField()

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
