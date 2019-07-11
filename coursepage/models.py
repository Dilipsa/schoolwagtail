from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class CoursePage(Page):
    template = "course/course_page.html"

    course_name = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel("course_name")
    ]
    class Meta:
        verbose_name = "Course Page"
        verbose_name_plural = "Course Pages"
