from django.db import models
from core.models import TimeStampedModel

from users.models import User


# Create your models here.
class Message(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    # Real chat application I think some char limits would be appropriate
    message = models.TextField(null=False, blank=False, default='')

    class JSONAPIMeta:
        resource_name = "messages"
