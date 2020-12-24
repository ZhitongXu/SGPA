from django.db import models
from django.conf import settings


class Keyword(models.Model):
    title = models.CharField(max_length=500)
    type = models.CharField(max_length=500, choices=settings.KEYWORD_CHOICES, verbose_name='关键词分类', null=True, blank=True)

    def __str__(self):
        return self.title
