from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import ListingSerializer
from .models import Listing


# /listing POST, GET
class ListingSet(generics.ListCreateAPIView):
    queryset = Listing.objects.all().order_by('id')
    serializer_class = ListingSerializer

# /listing/:id GET, UPDATE/EDIT, DELETE
class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all().order_by('id')
    serializer_class = ListingSerializer 