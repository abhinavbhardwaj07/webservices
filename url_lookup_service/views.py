# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .serializers import UserSerializer
from .models import MaliciousUrlsDetails
from rest_framework.views import APIView
from django.contrib.auth.models import User
from mongoengine.errors import DoesNotExist
from rest_framework.response import Response
import rest_framework_mongoengine.viewsets as mongo_viewsets

# Create your views here.


class Index(APIView):
    """
    Returns the default response
    """

    def get(self, request):
        return Response({
                        "ping": True,
                        "success": True
                    })


class UserList(APIView):
    """
    Returns all the users
    """

    def get(self, request):
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return Response(serializer.data)


class ResourceDetails(mongo_viewsets.ReadOnlyModelViewSet):
    """
    Retrieves the provided url information and Returns weather url is malicious or not
    """

    def retrieve(self, request, *args, **kwargs):
        try:
            record = MaliciousUrlsDetails.objects.get(host=kwargs.get("host"), port=kwargs.get("port"), original_path=kwargs.get("original_path"))
            data = {
                "success": True,
                "host": record["host"],
                "port": record["port"],
                "original_path": record["original_path"],
                "is_malicious": True
            }
        # As we maintain only malicious urls in the db. If not present in db its not malicious
        except DoesNotExist:
            data = {
                "success": True,
                "host": kwargs.get("host"),
                "port": kwargs.get("port"),
                "original_path": kwargs.get("original_path"),
                "is_malicious": False
            }

        response = Response(data)
        return response






