#! myproject.adapter.py
from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.signals import pre_social_login
from allauth.account.utils import perform_login
from django.dispatch import receiver
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    @receiver(pre_social_login)
    def link_to_local_user(sender, request, sociallogin, **kwargs):
        email_address = sociallogin.account.extra_data['email']
        users = User.objects.filter(email=email_address)
        if users:
            perform_login(request, users[0], email_verification=settings.ACCOUNT_EMAIL_VERIFICATION)
            raise ImmediateHttpResponse(redirect(settings.LOGIN_REDIRECT_URL))
