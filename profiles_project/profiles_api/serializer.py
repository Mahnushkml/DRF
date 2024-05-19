from rest_framework import serializers
from .models import UserProfile , ProfileFeedItem
import datetime

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # test = serializers.SerializerMethodField()
    class Meta:
        model=UserProfile
        fields = ('id', 'email','name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        # read_only_fields = ("date","username")

    def get_test(self):
        pass

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']

        )

        # validated_data["date"] = datetime.datetime.now()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = ProfileFeedItem
        fields = ('id','user_profile','status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only': True}}