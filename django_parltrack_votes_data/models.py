# -*- coding:Utf-8 -*-

# This file is part of django-parltrack-votes-data.
#
# django-parltrack-votes-data is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or any later version.
#
# django-parltrack-votes-data is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Affero Public
# License along with Foobar.
# If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2013  Laurent Peuch <cortex@worlddomination.be>

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
