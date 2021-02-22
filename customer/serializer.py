from rest_framework import serializers
from .models import CustomerProfile,MyRides


class CustomerProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	CustomerProfile
		fields 		=	"__all__"


class MyRideSerializer(serializers.ModelSerializer):
	class Meta:
		model 		=	MyRides
		fields 		=	"__all__"