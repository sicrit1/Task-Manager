from django.db import models
from django.utils.translation import gettext_lazy as _


class Statuses(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_('name'),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation date'),
    )

    def __str__(self):
        return self.name
