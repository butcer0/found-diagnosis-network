from django.db import models

from .constants import REVIEW_STATUS


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
    has_siblings = models.BooleanField()
    env_exposures = models.ManyToManyField(EnvExposure)
    gene_mutations = models.ManyToManyField(GeneMutation)
    reviewed_status = models.CharField(
        max_length=255,
        choices=[(tag, tag.value) for tag in REVIEW_STATUS],
        default=REVIEW_STATUS.NOT_REVIEWED)

    def __str__(self):
        return self.name
