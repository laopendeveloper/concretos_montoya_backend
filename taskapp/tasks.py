  
"""Celery tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone

# Models
from users.models import User

# Celery
from celery.decorators import task, periodic_task

# Utilities
import jwt
import time
from datetime import timedelta


def gen_verification_token(user):
    """Create JWT token that the user can use to verify its account."""
    exp_date = timezone.now() + timedelta(days=3)
    payload = {
        'user': user.username,
        'exp': int(exp_date.timestamp()),
        'type': 'email_confirmation'
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token.decode()

@task(name='send_confirmation_email', max_retries=3)
def send_confirmation_email(user_pk):
    """Send account verification link to given user."""
    user = User.objects.get(pk=user_pk)
    verification_token = gen_verification_token(user)
    subject = 'Bienvenido @{}! Verigfica tu cuenta para comenzar a usar Concretos Montoya App'.format(user.username)
    from_email = 'Concretos Montoya <noreply@concretosmontoya.com>' # concretosmontoya@hotmail.com
    content = render_to_string(
        'emails/users/account_verification.html',
        {'token': verification_token, 'user': user}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [user.email])
    msg.attach_alternative(content, "text/html")
    msg.send()

@periodic_task(name='project_mailstone_notification', run_every=timedelta(minutes=20))
def project_mailstone_notification():
    """Notify when a maistone arrives."""
    now = timezone.now()
    offset = now + timedelta(minutes=20)
    print('Periodic task')
    print(now)
    print(offset)

    # Update mailstones that have already finished
    #mailstone = ProjectMailstones.objects.filter(
    #    arrival_date__gte=now,
    #    arrival_date__lte=offset,
    #    is_active=True
    #)

    #mailstone.update(is_active=False)
