from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CustomerProfileSerializer,MyRideSerializer
from .models import CustomerProfile,MyRides

# Create your views here.


class CustomerProfileCreateAPIView(generics.CreateAPIView):
	serializer_class 		=	CustomerProfileSerializer
	queryset 				=	CustomerProfile.objects.all()



class CustomerProfileRetrieve(generics.RetrieveUpdateDestroyAPIView):
	serializer_class 	=		CustomerProfileSerializer
	lookup_field 		=		"id"
	queryset 			=		CustomerProfile.objects.all()
	# def get_queryset(self):
	# 	print(self.request.user)
	# 	query 		=		self.request.user.customerprofile
	# 	serialize 	=		CustomerProfileSerializer(query)
	# 	return 	query


class MyRidesAPIView(generics.ListCreateAPIView):
	serializer_class	=	MyRideSerializer
	queryset 			=	MyRides.objects.all()

	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)

	def perform_create(self,serializer):
		customer 	=	self.request.user.customerprofile
		serializer(customer=customer)

	def get(self,request):
		request 	=		self.request
		status 		=		self.request.GET.get('status')
		customer 	=		request.user.customerprofile
		query 		=		MyRides.objects.filter(customer=customer,ride_status=status)
		serialize 	=		MyRideSerializer(query,many=True)
		return Response(serialize.data)




