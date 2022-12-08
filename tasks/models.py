from django.db import models
from django.utils.translation import gettext_lazy as _

from statuses.models import Statuses
from django.contrib.auth import get_user_model


User = get_user_model()


class Tasks(models.Model):
    name = models.CharField(
        unique=True,
        max_length=200,
        verbose_name=_('name'),
    )
    description = models.TextField(
        blank=True,
        max_length=400,
        verbose_name=_('description'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author',
        verbose_name=_('author'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        verbose_name=_('executor'),
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        verbose_name=_('status'),
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation date'),
    )


    def __str__(self) -> str:
        """Return name of the task."""
        return self.name