# -*- coding: utf-8 -*-

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .template import Template


class Category(models.Model):

    name = models.CharField(_("Name"), max_length=400)
    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE,
        verbose_name=_("Template"),
        related_name="categories",
    )
    order = models.IntegerField(_("Display order"), blank=True, null=True)
    description = models.CharField(
        _("Description"), max_length=2000, blank=True, null=True
    )

    class Meta(object):
        # pylint: disable=too-few-public-methods
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def slugify(self):
        return slugify(str(self))
