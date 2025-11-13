from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    PENDING = "pending", _("Pending")
    SENT = "sent", _("Sent")
    FAILED = "failed", _("Failed")


class Channel(models.TextChoices):
    SMS = "sms", _("SMS")
    EMAIL = "email", _("Email")
    TELEGRAM = "telegram", _("Telegram")


class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    initial_channel = models.CharField(
        max_length=20, choices=Channel.choices, default=Channel.EMAIL
    )
    actual_channel = models.CharField(
        max_length=20, choices=Channel.choices, blank=True, null=True
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    retry_num = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "notification"
