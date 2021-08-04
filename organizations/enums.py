from django.db import models


class EmailStatuses(models.TextChoices):
    """
    Statues an email message can have
    """
    SENT = 'SUCCESS', 'success'
    FAILED = 'FAILURE', 'failure'
