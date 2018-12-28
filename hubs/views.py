from django.shortcuts import render
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
# from django_filters.rest_framework import DjangoFilterBackend
# import django_filters.rest_framework

from hubs.models import Hubs
from hubs.serializers import HubSerializer
from .forms import HubsForm


class HubsListView(generics.ListAPIView):
    serializer_class = HubSerializer
    queryset = Hubs.objects.all()
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name',)

    # def get_queryset(self):
    #     user = self.kwargs['name']
    #     return Hubs.objects.filter(name)


class HubsListCreateView(generics.ListCreateAPIView):
    serializer_class = HubSerializer
    queryset = Hubs.objects.all()


class HubsRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HubSerializer
    queryset = Hubs.objects.all()


# class HubsListView (generics.ListAPIView):
#     serializer_class=HubSerializer
#     queryset=Hubs.objects.all ()
    # renderer_classes=[TemplateHTMLRenderer]
    # template_name='hubs.html'
    #
    # def get(self, request):
    #     queryset = Hubs.objects.all()
    #     return render(request, 'hubs.html', {'hubs': queryset})
    #

# def form(request):
#     form = HubsForm()
#     return render (request, 'hubs.html', {'form': form})