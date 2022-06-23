from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class RecomendationReview(models.TextChoices):
    MUST_WATCH = "Must Watch"
    SHOULD_WATCH = "Should Watch"
    AVOID_WATCH = "Avoid Watch"
    NO_OPINION = "No Opinion"


# Create your models here.
class Review(models.Model):
    stars = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(
        max_length=50,
        choices=RecomendationReview.choices,
        default=RecomendationReview.NO_OPINION,
    )

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="reviews"
    )

    critic = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
