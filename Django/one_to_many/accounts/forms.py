from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    
    # age = forms.IntegerField(min_value=12, max_value=150, required=False)

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'age')
        fields = UserCreationForm.Meta.fields # + ('first_name', 'last_name', 'age')