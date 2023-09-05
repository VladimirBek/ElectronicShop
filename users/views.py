from django.contrib.auth.views import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.views.generic import UpdateView, CreateView, View

from users.forms import CustomUserChangeForm, CustomCreationForm
from users.models import User
from users.services import send_email_verify

class ProfileUpdateView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class UserCreate(CreateView):
    model = User
    form_class = CustomCreationForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:user_verify')

    def form_valid(self, form):
        self.object = form.save()
        send_email_verify(self.request, self.object)
        self.object.is_active = False
        form.save()

        return super().form_valid(form)


class EmailVerify(View):
    User = get_user_model()

    def get(self, request, uidb64):
        user = self.get_user(uidb64)

        user.is_active = True
        user.save()
        return redirect('catalog:index')

    def get_user(self, uidb64):
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
        return user
