#! myproject.adapter.py
from allauth.exceptions import ImmediateHttpResponse
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.signals import pre_social_login
from allauth.account.utils import perform_login
from django.dispatch import receiver
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.models import User


class MyLoginAccountAdapter(DefaultAccountAdapter):
    '''
    Overrides allauth.account.adapter.DefaultAccountAdapter.ajax_response to avoid changing
    the HTTP status_code to 400
    '''

    def get_login_redirect_url(self, request):
        if request.user.is_authenticated():
            return settings.LOGIN_REDIRECT_URL.format(
                id=request.user.id)
        else:
            return "/"


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    '''
    Overrides allauth.socialaccount.adapter.DefaultSocialAccountAdapter.pre_social_login to
    perform some actions right after successful login
    '''
    def pre_social_login(self, request, sociallogin):
        pass    # TODOFuture: To perform some actions right after successful login


@receiver(pre_social_login)
def link_to_local_user(sender, request, sociallogin, **kwargs):
    email_address = sociallogin.account.extra_data['email']
    users = User.objects.filter(email=email_address)
    if users:
        perform_login(request, users[0], email_verification=settings.ACCOUNT_EMAIL_VERIFICATION)
        raise ImmediateHttpResponse(redirect(settings.LOGIN_REDIRECT_URL))
