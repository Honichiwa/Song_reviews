from django.shortcuts import render
from rest_framework import generics
from . import models, serializers


class SongReviewList(generics.ListAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
