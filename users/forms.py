from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from catalog.forms import MixinFormStile
from users.models import User


class CustomAuthenticationForm(AuthenticationForm, MixinFormStile):
    class Meta:
        model = User
        fields = ('email', 'password',)


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'country')
