from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    APP_SUPPORT = 'App support'
    PAYMENT_SUPPORT = 'Payment support'
    HR_JOBS = 'HR/Jobs'
    OTHER = 'other'
    SUBJECT = [
        (APP_SUPPORT, _('App support')),
        (PAYMENT_SUPPORT, _('Payment support')),
        (HR_JOBS, _('HR/Jobs')),
        (OTHER, _('Other'))
    ]

    NEW = 'New'
    IN_PROGRESS = 'In progress'
    RESOLVED = 'Resolved'
    STATUS = [
        (NEW, _('New')),
        (IN_PROGRESS, _('In progress')),
        (RESOLVED, _('Resolved')),
    ]

    name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=255, validators=[EmailValidator], blank=False, null=False)
    subject = models.CharField(max_length=255, choices=SUBJECT, blank=False, null=False)
    message = models.TextField(max_length=500, blank=False, null=False)
    status = models.CharField(max_length=255, choices=STATUS)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"
