from rest_framework import serializers
from . import models


class SongReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    review = serializers.ReadOnlyField(source='review.id')

    class Meta:
        model = models.SongReviewComment
        fields = ['id', 'user', 'user_id', 'review', 'content']


class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = SongReviewCommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    def get_like_count(self, obj):
        return models.SongReviewLike.objects.filter(review=obj).count()

    def get_comment_count(self, obj):
        return models.SongReviewComment.objects.filter(review=obj).count()

    class Meta:
        model = models.SongReview
        fields = ['id', 'user', 'user_id','song', 'content', 'score', 'like_count','comment_count','comments']


class SongReviewLkeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SongReviewLike
        fields = ['id']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = ['id', 'name', 'duration', 'band', 'cover']