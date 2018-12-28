# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

# Create your models here.
from django.utils import timezone

from assets.models import Assets
from hubs.models import Hubs


class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    source = models.ForeignKey(Hubs, related_name='HubSrc')
    destination = models.ForeignKey(Hubs, related_name='HubDst')
    asset = models.ForeignKey(Assets, blank=True, null=True)
    weight = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    # billing_address = models.ForeignKey()
    cargo_description = models.CharField(blank=True, null=True, max_length=256)

    class Meta:
        ordering = ['source', 'destination']

    def __str__(self):
        return "{} - {}".format(self.source.name, self.destination.name)


