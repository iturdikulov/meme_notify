from django.db import models
# from django.contrib.postgres.fields import JSONField

class Status(models.TextChoices):
    PENDING = 'pending', 'Pending'
    SENT = 'sent', 'Sent'
    FAILED = 'failed', 'Failed'

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    priority = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    class Meta:
        db_table = 'notification'

# class NotificationRecipient(models.Model):
#     notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
#     user_id = models.BigIntegerField()
#     channel = models.CharField(max_length=20, choices=[('sms', 'SMS'), ('email', 'Email'), ('telegram',
# 'Telegram')])
#     recipient_address = models.CharField(max_length=255)
#     status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('sent', 'Sent'), ('failed',
# 'Failed')], default='pending')
#     sent_at = models.DateTimeField(null=True, blank=True)
#     delivered_at = models.DateTimeField(null=True, blank=True)
#     error_message = models.TextField(null=True, blank=True)
#     retry_count = models.IntegerField(default=0)
#
#     class Meta:
#         db_table = 'notification_recipient'
#
# class NotificationEvent(models.Model):
#     recipient = models.ForeignKey(NotificationRecipient, on_delete=models.CASCADE, related_name='events')
#     action = models.CharField(max_length=20, choices=[('sent', 'Sent'), ('failed', 'Failed'), ('retried',
# 'Retried')])
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = 'notification_event'
#
# class NotificationSettings(models.Model):
#     user_id = models.BigIntegerField(unique=True)
#     email = models.CharField(max_length=255, null=True, blank=True)
#     phone = models.CharField(max_length=50, null=True, blank=True)
#     telegram_id = models.CharField(max_length=100, null=True, blank=True)
#     sms_enabled = models.BooleanField(default=False)
#     email_enabled = models.BooleanField(default=False)
#     telegram_enabled = models.BooleanField(default=False)
#     notification_preferences = JSONField(null=True, blank=True)
#     quiet_hours_start = models.TimeField(null=True, blank=True)
#     quiet_hours_end = models.TimeField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = 'notification_settings'
#
#
# class Priority(models.TextChoices):
#     LOW = 'low', 'Low'
#     MEDIUM = 'medium', 'Medium'
#     HIGH = 'high', 'High'
#
#
# class Channel(models.TextChoices):
#     SMS = 'sms', 'SMS'
#     EMAIL = 'email', 'Email'
#     TELEGRAM = 'telegram', 'Telegram'
#
# class Action(models.TextChoices):
#     SENT = 'sent', 'Sent'
#     FAILED = 'failed', 'Failed'
#     RETRIED = 'retried', 'Retried'
#     DELIVERED = 'delivered', 'Delivered'  # Added
#
# # In Notification:
# priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.LOW)
#
# # In Recipient:
# channel = models.CharField(max_length=20, choices=Channel.choices)
# status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
#
# # In Event:
# action = models.CharField(max_length=20, choices=Action.choices)
#
