from rest_framework import serializers
from .models import UserProfile
import datetime

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserSerializer(serializers.ModelSerializer):
    """Serializes a name field for testing our APIView"""
    test = serializers.SerializerMethodField()
    class Meta:
        model=UserProfile
        fields = ('name', 'email','is_active')
        read_only_fields = ("date","username")

    def get_test(self):
        pass
    def create(self, validated_data):
        validated_data["date"] = datetime.datetime.now()

        return super().create(validated_data)
