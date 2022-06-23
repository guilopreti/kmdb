from rest_framework import serializers
from users.models import User

from .models import Review


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
        read_only_fields = ["first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer()

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recomendation",
            "movie_id",
            "critic",
        ]
        read_only_fields = ["movie_id"]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
