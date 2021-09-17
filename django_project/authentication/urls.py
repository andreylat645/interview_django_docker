from django.urls import path
from .views import UserView
from .views import AbonentView



urlpatterns = [
    path('users/', UserView.as_view()),
    path('abonents/', AbonentView.as_view())
]