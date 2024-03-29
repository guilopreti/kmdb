from django.urls import path

from . import views

urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<int:movie_id>/", views.MovieParamsView.as_view()),
    path("movies/<int:movie_id>/reviews/", views.MovieReviewView.as_view()),
]
