from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page

class ContactPage(Page):
    template = "contact/contact_page.html"
    contact_no = models.IntegerField(default=0)
    address = models.TextField(blank=False,null=True)

    content_panels = Page.content_panels + [
        FieldPanel("contact_no"),
        FieldPanel("address")
    ]

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"
