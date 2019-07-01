import requests
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            url = f'https://api.github.com/orgs/{self.name}'

            resp = requests.get(url).json()

            if resp.get('message') == 'Not Found':
                return

            self.name = resp['name']
            self.url = resp['html_url']

            repos = requests.get(resp['repos_url']).json()
            for repo in repos:
                resp = requests.get(repo['contributors_url']).json()
                contributors = len(resp)
                Repo.objects.create(
                    stars=repo['stargazers_count'],
                    forks=repo['forks'],
                    contributors=contributors,
                    organization=self)


class Repo(models.Model):
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    contributors = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
