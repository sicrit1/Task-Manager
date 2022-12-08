from django.db import models
from django.utils.translation import gettext_lazy as _


class Labels(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name=_('name'),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation date'),
    )

    def __str__(self) -> str:
        return self.name