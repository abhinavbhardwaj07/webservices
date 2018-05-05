
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the User data
    """
    class Meta:
        model = User
        fields = ('id', 'username')



