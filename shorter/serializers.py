from rest_framework.serializers import ModelSerializer

from shorter.models import URL


class ShorterSerializer(ModelSerializer):
    class Meta:
        model = URL
        fields = ['initial_url', 'short_url']
        required_fields = ['initial_url']
