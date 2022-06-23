import ipdb
from django.shortcuts import get_list_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Response, status
from reviews.serializers import ReviewSerializer

from .models import Movie
from .permissions import MoviePermission
from .serializers import MovieSerializer


# Create your views here.
class MovieView(APIView):
    permission_classes = [MoviePermission]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        movies = get_list_or_404(Movie)

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class MovieParamsView(APIView):
    permission_classes = [MoviePermission]

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)

            serializer = MovieSerializer(movie)

            return Response(serializer.data)
        except:
            return Response(
                {"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)

            movie.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"message": "Movie not fount."}, status=status.HTTP_404_NOT_FOUND
            )

    def patch(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)

            serializer = MovieSerializer(movie, request.data, partial=True)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response(serializer.data)
        except:
            return Response(
                {"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND
            )


class MovieReviewView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            user = request.user

            request.data["critic"] = user.__dict__

            serializer = ReviewSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(movie=movie, critic=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(
                {"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)

            reviews = movie.reviews

            serializer = ReviewSerializer(reviews, many=True)

            return Response(serializer.data)
        except:
            return Response(
                {"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND
            )
