from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def send_email_view(request):
    send_mail(
        'Subject here',       # Subject of the email
        'Here is the message.',  # Message of the email
        'example@gmail.com',   # Sender's email address
        ['to@example.com'],   # List of recipient(s)
        fail_silently=False,  # Whether to raise an exception if sending fails
    )
    return HttpResponse('Email sent successfully!')
