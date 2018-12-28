# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
from django.utils import timezone


class Assets(models.Model):
    id = models.UUIDField (primary_key=True, default=uuid.uuid4, editable=False)
    created_at=models.DateTimeField (default=timezone.now)
    updated_at=models.DateTimeField (default=timezone.now)

    length = models.DecimalField(max_digits=27, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=32)
    # weight = models.

    class Meta:
        ordering = ['type', 'length']

    def __str__(self):
        # return str(self.type)
        return str(self.type.encode('utf8', 'ignore'))