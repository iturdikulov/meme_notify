from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from up.models import Channel


class Status(models.TextChoices):
    PENDING = "pending", _("Pending")
    PROCESSED = "processed", _("Processed")


class NotificationGenerator(models.Model):
    initial_channel = models.CharField(
        max_length=20, choices=Channel.choices, default=Channel.TELEGRAM
    )
    notifications_amount = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10000)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notification_generator"
