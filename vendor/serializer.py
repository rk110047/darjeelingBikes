from rest_framework import serializers
from .models import VendorProfile,BikeDetails,BikeImages
from superadmin.serializer import StateSerializer,CitySerializer,BikeCompanySerializer,BikeModelSerializer




class BikeSerializer(serializers.ModelSerializer):

	bike_company 					=		BikeCompanySerializer()
	bike_model_name 				=		BikeModelSerializer()
	class Meta:
		model  		=		BikeDetails
		fields 		=	"__all__"