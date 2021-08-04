from celery import shared_task

from django.core.mail import send_mail

from organizations import enums, models


@shared_task
def task(content, receiver, sender):
    try:
        send_mail(
            'پیش فاکتور',
            'پیش فاکتور سازمان' + receiver,
            'django2021.1400@gmail.com',
            ['rezaee.sepehr007@gmail.com'],
            html_message=content,
        )
        models.EmailHistory.objects.create(sender=sender, receiver=receiver, status=enums.EmailStatuses.SENT)
    except:
        models.EmailHistory.objects.create(sender=sender, receiver=receiver, status=enums.EmailStatuses.FAILED)
    return None
