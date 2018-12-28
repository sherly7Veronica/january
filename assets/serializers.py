from rest_framework import serializers

from assets.models import Assets


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('__all__')


class AssetQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = ('length', 'type')