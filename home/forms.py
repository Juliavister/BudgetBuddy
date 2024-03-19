from django import forms
from .models import UserProfile
from .models import UploadPhoto

"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profession', 'Savings', 'income', 'image']

"""

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = UploadPhoto
        fields = ['photo', 'caption']



