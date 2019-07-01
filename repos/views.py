from rest_framework import generics

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *


class OrganizationView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


@csrf_exempt
def organization_repos(request, org_pk):
    """
    List all repos from an organization
    """
    if request.method == 'GET':
        org = Organization.objects.get(pk=org_pk)
        repos = org.repo_set.all()
        serializer = RepoSerializer(repos, many=True)
        return JsonResponse(serializer.data, safe=False)