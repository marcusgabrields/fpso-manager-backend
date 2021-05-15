from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedModel


class Vessel(TimeStampedModel):
    code = models.CharField(_("code"), max_length=10, unique=True)
