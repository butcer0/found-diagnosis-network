from django.db import models

from .constants import REVIEW_STATUS_CHOICES, REVIEW_STATUS_NOT_REVIEWED


class EnvExposure(models.Model):
    exposure_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.exposure_name


class GeneMutation(models.Model):
    gene_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.gene_name


class Participant(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    has_siblings = models.BooleanField(default=False)
    env_exposures = models.ManyToManyField(EnvExposure)
    gene_mutations = models.ManyToManyField(GeneMutation)
    reviewed_status = models.CharField(
        max_length=255,
        choices=REVIEW_STATUS_CHOICES,
        default=REVIEW_STATUS_NOT_REVIEWED)

    def __str__(self):
        return self.name
