from celery import shared_task
from django.core.mail import send_mail
from vpn.celery import app


@app.task
def send_email_task(subject, message, recipient_list):
    from_email = 'teamchallangechat@ukr.net'
    send_mail(subject, message, from_email, recipient_list)