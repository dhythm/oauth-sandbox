from django.db import models


class Token(models.Model):
    access_token = models.CharField(max_length=2047)
    expires_in = models.IntegerField()
    geolocation = models.CharField(max_length=255)
    id_token = models.CharField(max_length=2047)
    refresh_token = models.CharField(max_length=255)
    refresh_expires_in = models.IntegerField()
    scope = models.CharField(max_length=255)
    token_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.access_token
