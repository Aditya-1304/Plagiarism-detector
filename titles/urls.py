from django.urls import path
from .views import check_similarity

urlpatterns = [
    path('', check_similarity, name='check_similarity'),
]
