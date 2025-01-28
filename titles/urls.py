# titles/urls.py
from django.urls import path
from .views import check_similarity

urlpatterns = [
    path('check-similarity/', check_similarity, name='check_similarity')
]
