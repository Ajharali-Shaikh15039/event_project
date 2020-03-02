from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, BrandPageView, DigitalPageView, ClientsPageView, SocialmediaPageView, VirtualtourPageView

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('aboutus/',AboutPageView.as_view(), name = 'aboutus'),
	path('contactus/',ContactPageView.as_view(), name = 'contactus'),
	path('brand/',BrandPageView.as_view(), name = 'brand'),
	path('digital/',DigitalPageView.as_view(), name = 'digital'),
	path('ourclients/',ClientsPageView.as_view(), name = 'ourclients'),
	path('socialmedia/',SocialmediaPageView.as_view(), name = 'socialmedia'),
	path('virtualtour/',VirtualtourPageView.as_view(), name = 'virtualtour'),
	
]