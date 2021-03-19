from django.shortcuts import render
from .serializer import BikeSerializer
from rest_framework import generics
from .models import VendorProfile,BikeDetails,BikeImages
from django.contrib.auth.decorators import login_required
from .forms import VendorProfileForm,BikeForm,VendorProfileCreateForm


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


@login_required(login_url="login")
def vendors(request):
	query 	=	VendorProfile.objects.all()
	return render(request,'vendors.html',{'ls':query})



@login_required(login_url="login")
def vendor_profile_create(request):
	form 	=	VendorProfileCreateForm()
	if request.method=="POST":
		form 	=		VendorProfileCreateForm(request.POST,request.FILES)
		print(form.is_valid())
		if form.is_valid():
			form.save()
	return render(request,'vendor-profile-create.html',{'form':form})



@login_required(login_url="login")
def vendor_profile(request):
	user 	=	request.user
	query 	=	VendorProfile.objects.get(user=user)
	form 	=	VendorProfileForm(instance=query)
	if request.method=="POST":
		form 	=		VendorProfileForm(request.POST,request.FILES,instance=query)
		print(form.is_valid())
		if form.is_valid():
			form.save()
	return render(request,'vendor-profile.html',{'obj':query,'form':form})

@login_required(login_url="login")
def bike_create(request):
	vendor 	=	request.user.vendorprofile.id
	form 	=	BikeForm()
	if request.method=="POST":
		form 	=	BikeForm(request.POST,request.FILES)
		if form.is_valid():
			form.vendor = vendor
			form.save()
	return render(request,'bike-create.html',{'form':form})

@login_required(login_url="login")
def my_bikes(request):
	vendor 	=	request.user.vendorprofile.id
	query 	=	BikeDetails.objects.filter(vendor=vendor)
	return render(request,'my-bikes.html',{'ls':query})


@login_required(login_url="login")
def bike_edit(request,id=None):
	vendor 	=	request.user.vendorprofile.id
	bike 	=	BikeDetails.objects.get(id=id)
	form 	=	BikeForm(instance=bike)
	if request.method=="POST":
		form 	=	BikeForm(request.POST,request.FILES,instance=bike)
		if form.is_valid():
			form.save()
	return render(request,'bike-edit.html',{'form':form})
