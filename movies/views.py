from django.shortcuts import get_list_or_404
from rest_framework.views import APIView, Response, status

from .models import Movie
from .serializers import MovieSerializer


# Create your views here.
class MovieView(APIView):
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
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)

            serializer = MovieSerializer(movie)

            return Response(serializer.data)
        except:
            return Response(
                {"message": "Movie not found."}, status=status.HTTP_404_NOT_FOUND
            )
