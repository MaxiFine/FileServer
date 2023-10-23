from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2',)


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# # USING A CUSTOM LOGIN FOR USERNAME AND EMAIL
# class CustomAuthenticationForm(AuthenticationForm):
#     email_or_username = forms.CharField(label='Email or Username:')

#     def clean(self):
#         email_or_username = self.cleaned_data.get('email_or_username')
#         password = self.cleaned_data.get('password')
#         if email_or_username:
#             try:
#                 user = CustomUser.objects.get(email=email_or_username)
#             except CustomUser.DoesNotExist:
#                 try:
#                     user = authenticate(email=email_or_username)


