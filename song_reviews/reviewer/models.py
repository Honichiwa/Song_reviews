from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Band(models.Model):
    name = models.CharField(_("name"), max_length=250)

    class Meta:
        verbose_name = _("band")
        verbose_name_plural = _("bands")

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse("band_detail", kwargs={"pk": self.pk})


class Song(models.Model):
    name = models.CharField(_("name"), max_length=250)
    duration = models.PositiveIntegerField(_("duration"))
    band = models.ForeignKey(
        Band, 
        verbose_name=_("band"),
        on_delete=models.CASCADE,
        related_name="songs",
    )
    cover = models.ImageField(_("cover"),
        upload_to='songs/covers',
        null=True, blank=True,
    )
    class Meta:
        verbose_name = _("song")
        verbose_name_plural = _("songs")

    def __str__(self):
        return f'{self.name}, {self.band}'

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"pk": self.pk})
    

class SongReview(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='song_reviews',
    )
    song = models.ForeignKey(
        Song, verbose_name=_("song"), 
        on_delete=models.CASCADE,
        related_name='reviews'      
    )
    content = models.TextField(_("content"), max_length=10000)
    SCORE = ((i, f'{i}/10') for i in range(0, 11))
    score = models.PositiveSmallIntegerField(_("score"), choices=SCORE, default=0)
    class Meta:
        verbose_name = _("song review")
        verbose_name_plural = _("song reviews")

    def __str__(self):
        return f'{self.user}, {self.content}, {self.score}'

    def get_absolute_url(self):
        return reverse("songreview_detail", kwargs={"pk": self.pk})
    
    
class SongReviewComment(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='song_review_comments',
    )
    review = models.ForeignKey(
        SongReview,
        verbose_name=_("review"),
        on_delete=models.CASCADE,
        related_name='comments',
    )
    content = models.TextField(_("content"), max_length=1000)

    class Meta:
        verbose_name = _("song review comment")
        verbose_name_plural = _("song review comments")

    def __str__(self):
        return f'{self.user}, {self.review}, {self.content}'

    def get_absolute_url(self):
        return reverse("songreviewcomment_detail", kwargs={"pk": self.pk})


class SongReviewLike(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='song_review_likes',
    )
    review = models.ForeignKey(
        SongReview,
        verbose_name=_("song review like"),
        on_delete=models.CASCADE,
        related_name='likes',
    )
    class Meta:
        verbose_name = _("songreviewlike")
        verbose_name_plural = _("songreviewlikes")

    def __str__(self):
        return f'{self.user}, {self.review}'

    def get_absolute_url(self):
        return reverse("songreviewlike_detail", kwargs={"pk": self.pk})

    

