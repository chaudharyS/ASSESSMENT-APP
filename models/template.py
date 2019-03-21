from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Template(models.Model):
    name = models.CharField(_("Name"), max_length=400)
    description = models.TextField(_("Description"))

    class Meta(object):
        verbose_name = _("template")
        verbose_name_plural = _("templates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("template-detail", kwargs={"id": self.pk})
