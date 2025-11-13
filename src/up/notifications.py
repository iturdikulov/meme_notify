from time import sleep
import random

from config.settings import TASK_NOTIFICATION_MAX_RETRIES
from up.memes import PHOTOBOX_MEMES_RU
from up.models import Channel, Notification, Status


class AllSendMethodsFailedError(Exception):
    pass


def chance(percent):
    return random.random() < (percent / 100)


def send_sms() -> bool:
    """
    Sending SMS
    """

    sleep(random.uniform(1, 5))

    if chance(30):
        return True

    raise Exception("Failed to send message with random chance")



def send_email() -> bool:
    """
    Sending E-mail
    """

    sleep(random.uniform(1, 5))

    if chance(40):
        return True

    raise Exception("Failed to send message with random chance")


def send_telegram() -> bool:
    """
    Sending Telegram message
    """

    sleep(random.uniform(1, 5))

    if chance(50):
        return True

    raise Exception("Failed to send message with random chance")


def send_notification(initial_channel: Channel, retry_num: int) -> str:
    """
    Core sending logic
    Handles status updates and creates NotificationEvent entries.
    """

    # Prioritize initial_channel
    channels = [initial_channel]
    for channel in Channel.values:
        if channel not in channels:
            channels.append(channel)

    title, description = random.choice(PHOTOBOX_MEMES_RU)
    notification = Notification(
        title=title,
        message=description,
        initial_channel=channels[0],
        retry_num=retry_num,
    )

    for channel in channels:
        try:
            match Channel(channel):
                case Channel.TELEGRAM:
                    send_telegram()
                case Channel.EMAIL:
                    send_email()
                case Channel.SMS:
                    send_sms()

            notification.initial_channel = channels[0]
            notification.actual_channel = channel
            notification.status = Status.SENT
            notification.save()

            return f"Notification sent via {channel}"
        except Exception:
            print("fail")

    # Do not process for specific retries amount and generate notification
    if retry_num >= TASK_NOTIFICATION_MAX_RETRIES:
        notification.status = Status.FAILED
        notification.save()

    raise AllSendMethodsFailedError(
        f"Failed to send notification, channels: {channels}"
    )
