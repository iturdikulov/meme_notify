from django.db import models
from django.utils.translation import gettext_lazy as _

from up.models import Channel


class Status(models.TextChoices):
    PENDING = "pending", _("Pending")
    PROCESSED = "processed", _("Processed")


class NotificationGenerator(models.Model):
    channel = models.CharField(max_length=20, choices=Channel.choices, default=Channel.TELEGRAM)
    notifications_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notification_generator"
