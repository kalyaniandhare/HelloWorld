from django import forms
from .models import Extractore

class UserForm(forms.ModelForm):

    class Meta:
        model = Extractore
        fields = ('name', 'bank_name', 'email_id', 'password', )
