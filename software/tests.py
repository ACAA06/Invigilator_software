from django.test import TestCase
from django.core.mail import send_mail
# Create your tests here.
# Create your tests here.
send_mail(
    'Subject here',
    'Here is the message.',
    'clementjoe99@gmail.com',
    ['clementjoe99@gmail.com'],
    fail_silently=False,
)