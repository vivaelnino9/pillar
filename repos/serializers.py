from rest_framework import serializers
from .models import *


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = '__all__'
