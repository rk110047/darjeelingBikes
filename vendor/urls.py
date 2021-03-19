from django.urls import path
from .views import ReadyBikesAPIView,AllBikesAPIView,vendors,vendor_profile_create,vendor_profile,bike_create,my_bikes,bike_edit


urlpatterns=[
	path('list/',vendors,name='vendors'),
	path('create/',vendor_profile_create,name='vendor-profile-create'),
	path('profile/',vendor_profile,name="vendor-profile"),
	path('all-bikes/',AllBikesAPIView.as_view(),name='all-bikes'),
	path('ready-bikes/',ReadyBikesAPIView.as_view(),name='ready-bikes'),
	path('bike_create/',bike_create,name='bike-create'),
	path('my-bikes/',my_bikes,name='my-bikes'),
	path('bike-edit/<id>/',bike_edit,name='bike-edit')
]