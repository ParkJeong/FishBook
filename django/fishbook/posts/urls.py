from django.urls import path
from .views import new

urlpatterns = [
        path('new/', new, name="new"),
]
