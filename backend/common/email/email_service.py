
import os
from django.core.mail import send_mail

def send_email(subject: str, body: str, send_email: str) -> bool:
    '''
    Sends single email
    '''
    did_send = send_mail(
        subject, 
        body, 
        f'hello@{os.environ.get("BASE_HOST", default=True)}',
        [send_email],
        fail_silently=False,
    )
    return did_send
