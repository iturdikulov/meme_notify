from celery import group
from django.conf import settings
from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import redirect, render

from pages.models import NotificationGenerator
from up.models import Channel, Notification
from up.tasks import process_notification_group


def home(request):
    NotificationGeneratorFormSet = modelformset_factory(
        NotificationGenerator,
        fields=["initial_channel", "notifications_amount"],
    )

    if request.method == "POST":
        formset = NotificationGeneratorFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()

            for form in formset:
                group(
                    process_notification_group.s(
                        Channel(form.cleaned_data["initial_channel"])
                    )
                    for _ in range(form.cleaned_data["notifications_amount"])
                ).apply_async()

            messages.add_message(
                request, messages.INFO, "Notifications generated successfully."
            )
            return redirect("home")
    else:
        formset = NotificationGeneratorFormSet(
            queryset=NotificationGenerator.objects.none()
        )

    notifications = Notification.objects.all().order_by("-created_at")[:1000]
    context = {
        "debug": settings.DEBUG,
        "formset": formset,
        "notifications": notifications,
    }

    return render(request, "pages/home.html", context)
