from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
from django.utils import timezone


class Hubs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    name = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    @staticmethod
    def get_fields_list():
        return [
            'id',
            'name'
        ]
