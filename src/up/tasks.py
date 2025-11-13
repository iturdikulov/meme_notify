from celery import shared_task

from config.settings import (
    TASK_NOTIFICATION_MAX_RETRIES,
    TASK_NOTIFICATION_RETRY_DELAY,
)
from up.models import Channel

from .notifications import AllSendMethodsFailedError, send_notification


@shared_task(bind=True, default_retry_delay=TASK_NOTIFICATION_RETRY_DELAY)
def process_notification_group(self, initial_channel: Channel):
    """
    Process notifications with recipients
    Support retrying on specific exceptions
    """

    try:
        return send_notification(initial_channel, self.request.retries)
    except AllSendMethodsFailedError as e:
        raise process_notification_group.retry(
            exc=e, max_retries=TASK_NOTIFICATION_MAX_RETRIES
        )
