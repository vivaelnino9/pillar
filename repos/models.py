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

            headers = {
                'Authorization': 'ba8e15a38f6e1375ca4d594a5991f7b0c5b1c494',
            }

            resp = requests.get(url, headers=headers).json()

            if resp.get('message') == 'Not Found':
                self.delete()
                return

            self.name = resp['name']
            self.url = resp['html_url']

            repos = requests.get(resp['repos_url'], headers=headers).json()
            for repo in repos:
                raw_resp = requests.get(repo['contributors_url'], headers=headers)
                if raw_resp.status_code != 200:
                    continue

                contributors = len(raw_resp.json())
                Repo.objects.create(
                    name=repo['name'],
                    stars=repo['stargazers_count'],
                    forks=repo['forks'],
                    contributors=contributors,
                    organization=self)


class Repo(models.Model):
    name = models.CharField(max_length=30)
    stars = models.IntegerField(default=0)
    forks = models.IntegerField(default=0)
    contributors = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
