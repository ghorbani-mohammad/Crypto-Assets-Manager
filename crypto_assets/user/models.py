from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    mobile_number = models.SlugField(max_length=11, null=True, blank=True, unique=True)

    def __str__(self):
        return f"({self.pk} - {self.mobile_number})"

    @property
    def telegram_account(self):
        return self.telegram_accounts.last()


class TelegramAccount(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="telegram_accounts"
    )
    chat_id = models.IntegerField(unique=True)

    def __str__(self):
        return f"({self.profile.mobile_number} - {self.chat_id})"
