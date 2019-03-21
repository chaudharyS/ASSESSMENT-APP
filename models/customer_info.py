from django.db import models
from django.utils.translation import ugettext_lazy as _
from .template import Template

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employee_count = models.IntegerField()
    template = models.ForeignKey(
        Template,
        on_delete=models.PROTECT,
        verbose_name=_("Template"),
        blank=True,
        null=True,
        related_name="customers",
    )   
    class Meta(object):
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def __str__(self):
        return self.customer_name
