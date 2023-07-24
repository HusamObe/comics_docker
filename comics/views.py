from django.shortcuts import render
from .models import Comic
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ComicSerializer

class ComicListView(ListCreateAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer

class ComicDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
