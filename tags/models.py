from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
  label = models.CharField(max_length=255)

class TaggedItem(models.Model):
  tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveSmallIntegerField()
  content_object = GenericForeignKey()

  class Meta:
    verbose_name = 'Liked Item'
    verbose_name_plural = 'Liked Items'

