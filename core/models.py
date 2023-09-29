from django.db import models

# Create your models here.

class SeedStatus(models.TextChoices):
    OK = 'OK'
    INVALID = 'INVALID'

class Seed(models.Model):
    scan_id = models.IntegerField(null=False)
    row = models.IntegerField(null=False)
    col = models.IntegerField(null=False)
    status = models.CharField(
        max_length=10,
        choices=SeedStatus.choices,
        default=SeedStatus.OK
    )
    tags = models.ManyToManyField('Tag', related_name='seeds')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None, editable=False)

class Tag(models.Model):
    type = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    deleted = models.BooleanField(default=False)
    short_name = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True, default=None, editable=False)

    def __str__(self):
        return self.type