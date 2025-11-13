from django.conf import settings
from django.contrib import messages
from django.forms import modelformset_factory
from django.shortcuts import render
from django.shortcuts import redirect

from pages.models import NotificationGenerator


def home(request):
    NotificationGeneratorFormSet = modelformset_factory(
        NotificationGenerator, fields=["channel", "notifications_amount"]
    )

    if request.method == "POST":
        formset = NotificationGeneratorFormSet(request.POST or None, request.FILES)
        if formset.is_valid():
            formset.save()
            messages.add_message(
                request, messages.INFO, "Notifications generated successfully."
            )
    else:
        formset = NotificationGeneratorFormSet()

    context = {"debug": settings.DEBUG, "formset": formset}

    return render(request, "pages/home.html", context)
