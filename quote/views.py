# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from quote.models import Quote
from quote.serializers import QuoteSerializer


class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class QuoteListCreateView(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


class QuoteRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


# class QuoteListView(generics.ListAPIView):
#     serializer_class = QuoteSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'hubs.html'
#
#     def get(self, request):
#         queryset=Quote.objects.all ()
#
#         search_query=request.GET.get ('search_box', None)
#         return Response({'quotes': queryset})
