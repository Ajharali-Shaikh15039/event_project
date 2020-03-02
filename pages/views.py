from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
	template_name = 'home.html'

class AboutPageView(TemplateView):
	template_name = 'aboutus.html'

class ContactPageView(TemplateView):
	template_name = 'contactus.html'

class BrandPageView(TemplateView):
	template_name = 'brand.html'

class DigitalPageView(TemplateView):
	template_name = 'digital.html'

class ClientsPageView(TemplateView):
	template_name = 'ourclients.html'

class SocialmediaPageView(TemplateView):
	template_name = 'socialmedia.html'

class VirtualtourPageView(TemplateView):
	template_name = 'virtualtour.html'		