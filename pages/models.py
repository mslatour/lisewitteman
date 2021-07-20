from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.images.models import Image
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    book_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    tagline = models.TextField(default='')
    sub_tagline = models.TextField(default='')

    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        ImageChooserPanel('book_image'),
        ImageChooserPanel('profile_image'),
        FieldPanel('tagline'),
        FieldPanel('sub_tagline'),
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.live().in_menu()
        return context

class FullPage(Page):
    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(FullPage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.live().in_menu()
        return context

class NarrowPage(Page):
    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(NarrowPage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.live().in_menu()
        return context
