from rest_framework import serializers
from . import models


class SongReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'song', 'content', 'score']