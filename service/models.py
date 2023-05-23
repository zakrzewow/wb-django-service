from django.db import models


class DNAWindow(models.Model):
    chromosome = models.CharField(max_length=10)
    window_index = models.IntegerField()
    start_position = models.BigIntegerField()
    end_position = models.BigIntegerField()
    enhancer_probability = models.FloatField()

    def __str__(self):
        return f"DNAWindow [Chromosome={self.chromosome} Idx={self.window_index} Probability={self.enhancer_probability}"
