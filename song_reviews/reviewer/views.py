from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from . import models, serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class SongReviewList(generics.ListCreateAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class SongReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        post = models.SongReview.objects.filter(
            pk=kwargs['pk'],
            user=request.user
        )
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You have no rights to update this'))
        
    def delete(self, request, *args, **kwargs):
        post = models.SongReview.objects.filter(
            pk=kwargs['pk'],
            user=request.user
        )
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You have no rights to delete this'))
        

class SongReviewCommentList(generics.ListCreateAPIView):
    serializer_class = serializers.SongReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        review = models.SongReview.objects.get(pk=self.kwargs['songreview_pk'])
        serializer.save(user=self.request.user, review=review)
    
    def get_queryset(self):
        review = models.SongReview.objects.get(pk=self.kwargs['songreview_pk'])
        return models.SongReviewComment.objects.filter(review=review)
    

class SongReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SongReviewComment.objects.all()
    serializer_class = serializers.SongReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        try:
            comment = models.SongReviewComment.objects.get(pk=kwargs['pk'], user=request.user)
        except:
            raise ValidationError(_('You cannot update this'))
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        try:
            comment = models.SongReviewComment.objects.get(pk=kwargs['pk'], user=request.user)
        except Exception as e:
            raise ValidationError(_(f'You cannot delete this {e}'))
        return self.destroy(request, *args, **kwargs)

class SongReviewLikeCreateDestroy(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = serializers.SongReviewLkeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        review = models.SongReview.objects.get(pk=self.kwargs['pk'])
        return models.SongReviewLike.objects.filter(user=self.request.user, review=review)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError(_('You already liked this'))
        review = models.SongReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, review=review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError(_('You cannot unlike what you dont like'))

class SongList(generics.ListAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Song.objects.all()
    serializer_class = serializers.SongSerializer
    permission_classes = [permissions.IsAdminUser]