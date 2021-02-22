from django.urls import path
from .views import ReadyBikesAPIView,AllBikesAPIView


urlpatterns=[
	path('all-bikes/',AllBikesAPIView.as_view(),name='all-bikes'),
	path('ready-bikes/',ReadyBikesAPIView.as_view(),name='ready-bikes')
]