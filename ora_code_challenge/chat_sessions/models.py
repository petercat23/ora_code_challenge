from django.db import models
from users.models import User

from core.models import TimeStampedModel


class Session(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class JSONAPIMeta:
        resource_name = "sessions"
