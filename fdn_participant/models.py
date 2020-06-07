from django.db import models


class GeneMutation(models.Model):
    gene_name = models.CharField(max_length=200)

    def __str__(self):
        return self.gene_name
