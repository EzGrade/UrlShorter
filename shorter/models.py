from django.db import models


class URL(models.Model):
    short_url = models.CharField(max_length=16)
    initial_url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    auto_delete_date = models.DateTimeField(null=True, blank=True)
