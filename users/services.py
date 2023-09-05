from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, send_mail

from config import settings


def send_email_verify(request, user):
    current_site = get_current_site(request)
    domain = current_site.domain

    context = {
        'user': user,
        'domain': domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": token_generator.make_token(user)
    }
    message = render_to_string(
        'verify_email.html',
        context=context
    )
    send_mail(
        'Подтверждение регистрации',
        message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email]
    )
