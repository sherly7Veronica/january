from rest_framework import serializers

from assets.serializers import AssetQuoteSerializer
from hubs.serializers import HubQuoteSerializer
from quote.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    # source = HubQuoteSerializer()
    # destination = HubQuoteSerializer()
    # asset = AssetQuoteSerializer()

    class Meta:
        model = Quote
        # fields = ('source', 'destination', 'asset')
        fields = ('__all__')

    # def create(self, validated_data):
        # return Quote.objects.create(**validated_data)


# class QuoteRatesSerializer(serializers.ModelSerializer):
