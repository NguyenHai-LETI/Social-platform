from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email', 'full_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('full_name', 'phone_number', 'occupation', 'bio', 'avatar_url')
        exclude = ('password',)
        labels = {'full_name': 'Họ và tên'}
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }