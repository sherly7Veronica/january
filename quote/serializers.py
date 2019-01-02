from rest_framework import serializers

from assets.serializers import AssetQuoteSerializer
from hubs.serializers import HubQuoteSerializer
from quote.models import Quote


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ('id',
                  'source',
                  'destination',
                  'asset',
                  'weight',
                  'cargo_description')

    def create(self, validated_data):
        return Quote.objects.create(**validated_data)


class QuoteListSerializer(serializers.ModelSerializer):
    source = HubQuoteSerializer()
    destination = HubQuoteSerializer()
    asset = AssetQuoteSerializer()

    class Meta:
        model = Quote
        fields = ('__all__',)

