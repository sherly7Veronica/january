# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from assets.models import Assets
from assets.serializers import AssetSerializer


class AssetListView(generics.ListAPIView):
    serializer_class = AssetSerializer
    queryset = Assets.objects.all()


class AssetListCreateView(generics.ListCreateAPIView):
    serializer_class = AssetSerializer
    queryset = Assets.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = serializer.data
        return Response(response)


class AssetRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssetSerializer
    queryset = Assets.objects.all()



