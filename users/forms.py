from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms.models import ModelForm
from django.forms import ValidationError
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


class ForgotPasswordForm(ModelForm):

    def validate_unique(self):
        pass

    def clean_email(self):
        user_email = self.cleaned_data.get('email')
        if not User.objects.filter(email=user_email).exists():
            raise ValidationError('Пользователя с таким email не существует')
        return user_email

    class Meta:
        model = User
        fields = ('email',)
