from django import forms
from .models import Extractore, StoreData

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Extractore
        fields = ('name', 'bank_name', 'email_id', 'password', )
