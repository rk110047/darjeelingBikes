from django.shortcuts import render
from .serializer import BikeSerializer
from rest_framework import generics
from .models import VendorProfile,BikeDetails,BikeImages


# Create your views here.


class ReadyBikesAPIView(generics.ListAPIView):
	serializer_class 		=		BikeSerializer
	def get_queryset(self):
		query 		=		BikeDetails.objects.filter(approved=True,ready=True)
		return query


class AllBikesAPIView(generics.ListAPIView):
	serializer_class 		=		BikeSerializer
	def get_queryset(self):
		query 		=		BikeDetails.objects.filter(approved=True)
		return query
