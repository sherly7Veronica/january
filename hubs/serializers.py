from rest_framework import serializers

# from .models import Assets
from hubs.models import Hubs


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hubs
        fields = ('__all__')


class HubQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hubs
        fields = ('id', 'name')

