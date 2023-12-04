from django.db import models


class Country_2(models.Model):
    country = models.CharField("", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country

