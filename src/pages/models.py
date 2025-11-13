from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _

from up.models import Channel


class Status(models.TextChoices):
    PENDING = "pending", _("Pending")
    PROCESSED = "processed", _("Processed")


class NotificationGenerator(models.Model):
    channel = forms.ChoiceField(choices=Channel.choices)
    notifications_amount = forms.IntegerField(
        min_value=1, label="Number of notifications to generate"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notification_generator"
