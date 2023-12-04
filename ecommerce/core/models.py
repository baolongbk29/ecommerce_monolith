from django.db import models


class Country(models.Model):
    country = models.CharField("", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country


class State(models.Model):
    state = models.CharField("", max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, related_name='country_state')

    def __str__(self):
        return self.state


class City(models.Model):
    city = models.CharField("", max_length=100, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True, related_name='state_city')

    def __str__(self):
        return self.city