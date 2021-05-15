from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel


class Equipment(TimeStampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", _("active")
        INACTIVE = "inactive", _("inactive")
        UNDER_MAINTENANCE = "under_maintenance", _("under_maintenance")

    vessel = models.ForeignKey(
        "vessels.Vessel",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("vessel"),
    )
    name = models.CharField(_("name"), max_length=100)
    code = models.CharField(_("code"), max_length=100, unique=True)
    location = models.CharField(_("location"), max_length=100)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
