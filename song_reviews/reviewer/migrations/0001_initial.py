# Generated by Django 4.2.2 on 2023-06-13 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
            ],
            options={
                'verbose_name': 'band',
                'verbose_name_plural': 'bands',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('duration', models.PositiveIntegerField(verbose_name='duration')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='reviewer.band', verbose_name='band')),
            ],
            options={
                'verbose_name': 'song',
                'verbose_name_plural': 'songs',
            },
        ),
        migrations.CreateModel(
            name='SongReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000, verbose_name='content')),
                ('score', models.PositiveSmallIntegerField(choices=[(0, '0/10'), (1, '1/10'), (2, '2/10'), (3, '3/10'), (4, '4/10'), (5, '5/10'), (6, '6/10'), (7, '7/10'), (8, '8/10'), (9, '9/10'), (10, '10/10')], default=0, verbose_name='score')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviewer.song', verbose_name='song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_reviews', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'song review',
                'verbose_name_plural': 'song reviews',
            },
        ),
        migrations.CreateModel(
            name='SongReviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='reviewer.songreview', verbose_name='song review like')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_review_likes', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'songreviewlike',
                'verbose_name_plural': 'songreviewlikes',
            },
        ),
        migrations.CreateModel(
            name='SongReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=1000, verbose_name='content')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviewer.songreview', verbose_name='review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song_review_comments', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'song review comment',
                'verbose_name_plural': 'song review comments',
            },
        ),
    ]
