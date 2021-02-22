from django.urls import path
from .views import CustomerProfileCreateAPIView,CustomerProfileRetrieve,MyRidesAPIView


urlpatterns=[
	path('profile/create/',CustomerProfileCreateAPIView.as_view(),name='customer-profile-create'),
	path('profile/retrieve/<id>/',CustomerProfileRetrieve.as_view(),name='customer-profile-retrieve'),
	path('rides/',MyRidesAPIView.as_view(),name='my-rides-list-create')
]