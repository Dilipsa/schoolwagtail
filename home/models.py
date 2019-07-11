from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    templates = "home/home_page.html"
    max_count = 1
    name = models.CharField(max_length=100)
    about = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('about')
    ]
    class Meta:
        verbose_name="Dilip"
        verbose_name_plural="Dilips"
