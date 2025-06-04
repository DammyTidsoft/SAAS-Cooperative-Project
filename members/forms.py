from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member

class MemberForm(UserCreationForm):
    class Meta:
        model = Member
        fields = [
            'username', 'password1', 'password2',
            'full_name', 'sex', 'age', 'date_of_birth',
            'address', 'phone_number', 'email',
            'next_of_kin_name', 'next_of_kin_address', 'next_of_kin_phone',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = "Enter Password"
        self.fields['password2'].label = "Confirm Password"
