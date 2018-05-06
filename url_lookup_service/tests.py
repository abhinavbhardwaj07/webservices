# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import MaliciousUrlsDetails
from mongoengine.errors import DoesNotExist

# Create your tests here.
# for models file

class MaliciousUrlsDetailsTestCase(TestCase):
    def setUp(self):
        MaliciousUrlsDetails(host='127.0.0.1',port=8000,original_path='home/alone/testing',is_malicious=True).save()

    def test_url_is_maliciuos(self):
        """Urls can be identified as malicious"""
        h_object_1 = {}
        h_object_2 = {}
        try:
            h_object_1 = MaliciousUrlsDetails.objects.get(host='127.0.0.1',port=8000,original_path='home/alone/testing')
            h_object_2 = MaliciousUrlsDetails.objects.get(host='127.0.0.1',port=8000,original_path='home/alone5')
        except DoesNotExist:
            h_object_2['is_malicious'] = False
        self.assertEqual(h_object_1['is_malicious'], True)
        self.assertEqual(h_object_2['is_malicious'], False)
