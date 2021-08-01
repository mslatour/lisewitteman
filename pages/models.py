from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
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


class FullPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(default='')),
        ('logo_item', blocks.StructBlock([
            ('logo', ImageChooserBlock(required=True)),
            ('description', blocks.RichTextBlock()),
        ])),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]


class NarrowPage(Page):
    body = RichTextField(default='')

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
