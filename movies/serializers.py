from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField(style={"base_template": "textarea.html"})

    genres = GenreSerializer(many=True)

    def create(self, validated_data):
        if "genres" in validated_data.keys():
            genres = []

            for data in validated_data["genres"]:
                try:
                    genres.append(Genre.objects.get(name=data["name"].lower()))
                except:
                    genres.append(Genre.objects.create(name=data["name"].lower()))

        del validated_data["genres"]

        movie = Movie.objects.create(**validated_data)

        movie.genres.set(genres)

        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.premiere = validated_data.get("premiere", instance.premiere)
        instance.classification = validated_data.get(
            "classification", instance.classification
        )
        instance.synopsis = validated_data.get("synopsis", instance.synopsis)

        if "genres" in validated_data.keys():
            genres = []

            for data in validated_data["genres"]:
                try:
                    genres.append(Genre.objects.get(name=data["name"].lower()))
                except:
                    genres.append(Genre.objects.create(name=data["name"].lower()))

            instance.genres.set(genres)

        instance.save()
        return instance
