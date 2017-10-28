from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from core.models import TimeStampedModel


class UserManager(BaseUserManager):

    def create_user(self, username,  password):
        user = self.model(username=username.lower())
        user.set_password(password)
        user.save()

        return user

    def create_admin(self, username, password):
        admin = self.create_user(username, password)
        admin.is_admin = True
        admin.save()
        return admin


class User(AbstractBaseUser, TimeStampedModel):

    username = models.CharField(max_length=256)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    @property
    def is_staff(self):
        if self.is_admin:
            return True
        return False
