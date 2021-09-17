from django.urls import path
from .views import UserViewSet
from .views import AbonentViewSet


urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('abonents/', AbonentViewSet.as_view({'get': 'list'}))
]