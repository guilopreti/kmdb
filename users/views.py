from rest_framework.views import APIView, Response, status

from .models import User
from .serializers import UserSerializer


# Create your views here.
class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
