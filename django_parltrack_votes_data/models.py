# -*- coding:Utf-8 -*-
import json
from django.db import models


class VotesData(models.Model):
    proposal_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    imported = models.BooleanField(default=False)
    date = models.DateTimeField()
    data = models.TextField()

    def data_pretty(self):
        return json.dumps(json.loads(self.data), sort_keys=False, indent=4)

    class Meta:
        ordering = ['date', 'proposal_name']
