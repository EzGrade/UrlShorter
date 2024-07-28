from django.shortcuts import redirect
from rest_framework import viewsets
import secrets

from rest_framework.response import Response

from .models import URL
from .serializers import ShorterSerializer


class ShorterViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = ShorterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        short_url = secrets.token_urlsafe(16)
        serializer.save(short_url=short_url)
        return Response({'short_url': short_url})

    def retrieve(self, request, pk=None):
        url = URL.objects.get(short_url=pk)
        return redirect(url.initial_url)
