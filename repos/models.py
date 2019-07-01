from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=30)
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    contributors = models.IntegerField(default=0)

    def __str__(self):
        return self.name
