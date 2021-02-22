from django.urls import path
from .views import LoginWithTokenAuthenticationAPIView,RegisterAPIView,login_user,logout_user

urlpatterns=[
	path('',login_user),
	path('logout/',logout_user),
	path('login/',LoginWithTokenAuthenticationAPIView.as_view(),name='login'),
	path('register/',RegisterAPIView.as_view(),name='register')
]