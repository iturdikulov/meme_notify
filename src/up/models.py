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


class Action(models.TextChoices):
    SENT = "sent", _("Sent")
    FAILED = "failed", _("Failed")
    RETRIED = "retried", _("Retried")
    DELIVERED = "delivered", _("Delivered")


class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        db_table = "notification"


class NotificationRecipient(models.Model):
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    initial_channel = models.CharField(max_length=20, choices=Channel.choices)
    recipient_address = models.CharField(max_length=255)
    sent_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)
    retry_count = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        db_table = "notification_recipient"


class NotificationEvent(models.Model):
    recipient = models.ForeignKey(
        NotificationRecipient, on_delete=models.CASCADE, related_name="events"
    )
    action = models.CharField(max_length=20, choices=Action.choices)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notification_event"
