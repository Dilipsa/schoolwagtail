from django.utils import timezone
from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

class NotificationPage(Page):
    template = "notification/notification_page.html"

    carrier_post = models.CharField(max_length=200)
    carrier_subject = models.CharField(max_length=200)
    required = models.IntegerField(default=0)

    exam_for = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)

    event = models.CharField(max_length=200)
    fro = models.DateField(default=timezone.now)
    to = models.DateField(default=timezone.now)
    total = models.IntegerField(default=0)

    content_panels = Page.content_panels + [
        FieldPanel("carrier_post"),
        FieldPanel("carrier_subject"),
        FieldPanel("required"),

        FieldPanel("exam_for"),
        FieldPanel("date"),

        FieldPanel("event"),
        FieldPanel("fro"),
        FieldPanel("to"),
        FieldPanel("total")
    ]

    class Meta:
        verbose_name = "notification Page"
        verbose_name_plural = "notification Pages"
