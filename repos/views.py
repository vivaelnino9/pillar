from rest_framework import generics
from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
