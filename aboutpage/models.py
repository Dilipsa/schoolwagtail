from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

class AboutPage(Page):
    template = "about/about_page.html"

    school_name = models.CharField(max_length=200)
    school_address = RichTextField(blank=False,null=True)

    content_panels = Page.content_panels + [
        FieldPanel("school_name"),
        FieldPanel("school_address")
    ]
    class Meta:
        verbose_name = "about Page"
        verbose_name_plural = "about Pages"
