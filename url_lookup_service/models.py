# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from mongoengine import Document

from mongoengine import StringField, DateTimeField, IntField, BooleanField


# Create your models here.

class MaliciousUrlsDetails(Document):

    host = StringField()
    port = IntField()
    original_path = StringField()
    first_seen = DateTimeField(default=timezone.now)
    is_malicious = BooleanField(default=True)

    def __str__(self):
        return '{}:{}/{}'.format(self.host, self.port, self.original_path)

