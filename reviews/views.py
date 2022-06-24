from django.shortcuts import get_list_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Response, status

from .models import Review
from .permissions import ReviewPermission
from .serializers import ReviewSerializer


# Create your views here.
class ReviewView(APIView, PageNumberPagination):
    def get(self, request):
        reviews = get_list_or_404(Review)

        result_page = self.paginate_queryset(reviews, request, view=self)

        serializer = ReviewSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)


class ReviewParamsView(APIView):
    permission_classes = [ReviewPermission]

    def delete(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)

            review.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(
                {"message": "Review not found."}, status=status.HTTP_404_NOT_FOUND
            )
