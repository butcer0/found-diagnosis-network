from django.db import models


class GeneMutation(models.Model):
    gene_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.gene_name


class EnvExposure(models.Model):
    exposure_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.exposure_name
