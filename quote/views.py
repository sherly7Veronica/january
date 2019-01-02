# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from quote.models import Quote
from quote.serializers import QuoteSerializer, QuoteListSerializer


class QuoteListView(generics.ListAPIView):
    serializer_class = QuoteListSerializer
    queryset = Quote.objects.all()


class QuoteListCreateView(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()


# class QuoteRUDView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = QuoteSerializer
#     queryset = Quote.objects.all()


# class QuoteRatesListView(generics.RetrieveAPIView):
#     serializer_class = QuoteRatesSerializer

# front end quote view
# class QuoteListView(generics.ListAPIView):
#     serializer_class = QuoteSerializer
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'quote.html'
#
#     def get(self, request):
#         queryset=Quote.objects.all ()
#         src=Quote.objects.all()
#         dest=Quote.objects.all()
#
#         search_query=request.GET.get ('search_box', None)
#         return Response({'src': src,
#                          'dest': dest})
