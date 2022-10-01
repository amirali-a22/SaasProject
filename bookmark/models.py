from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        to=User,
        related_name='categories',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('bookmark:category_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='bookmarks'
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    visit_count = models.IntegerField(
        default=0,
    )
    created_by = models.ForeignKey(
        to=User,
        related_name='bookmarks',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def get_absolute_url(self):
        return reverse('bookmark:bookmark_detail', kwargs={'pk': self.id})

    def increase_visit_count(self):
        self.visit_count += 1
        self.save()

    def __str__(self):
        return self.title
