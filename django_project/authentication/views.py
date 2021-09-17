from rest_framework import viewsets
from rest_framework.response import Response

from .models import User
from .models import Abonent
from .serializers import UserSerializer
from .serializers import AbonentSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        r = Response(serializer.data)
        print("Status code: " + str(r.status_code))
        return r


class AbonentViewSet(viewsets.ViewSet):
    def list(self, request):
        abonents = Abonent.objects.all()
        serializer = AbonentSerializer(abonents, many=True)
        r = Response(serializer.data)
        print("Status code: " + str(r.status_code))
        return r
