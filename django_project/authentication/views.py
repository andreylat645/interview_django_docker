from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .models import Abonent
from .serializers import UserSerializer
from .serializers import AbonentSerializer



class UserView(APIView):
    def get(self, request):
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response({"users:": serializer.data})


class AbonentView(APIView):
    def get(self, request):
        abonents = Abonent.objects.all()

        serializer = AbonentSerializer(abonents, many=True)
        return Response({"abonents:": serializer.data})