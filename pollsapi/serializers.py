"""Pollsapi serializers."""

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from .models import Poll, Choice, Vote


class VoteSerializer(serializers.ModelSerializer):
    """VoteSerializer for representing vote model instances."""

    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    """Serializer for choice model instances"""

    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    """Serializer for Polls model instances."""

    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """create a user using only email and username fields."""
        # overriden the ModelSerializer method’s create() to save the User instances.
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


"""

• A "is_valid(self, ..)" method which can tell if the data is sufficient and valid to create/update a model
instance.

• A "save(self, ..)" method, which khows how to create or update an instance.

• A "create(self, validated_data, ..)" method which knows how to create an instance. This method
can be overriden to customize the create behaviour.

• A "update(self, instance, validated_data, ..)" method which knows how to update an in-
stance. This method can be overriden to customize the update behaviour.


"""