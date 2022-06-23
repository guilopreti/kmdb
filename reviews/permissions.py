from rest_framework import permissions

from .serializers import ReviewSerializer


class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        reviews = ReviewSerializer(request.user.reviews, many=True)

        for review in reviews.data:
            if review["id"] == view.kwargs["review_id"]:
                return True

        return request.user.is_superuser
