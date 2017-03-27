from django.http import HttpResponsePermanentRedirect
from others.models import Others
from others.serializers import OthersListSerializer, OthersDetailSerializer
from others.permissions import OthersPermission
from rest_framework import viewsets
from rest_framework.response import Response

class OthersViewSet(viewsets.ModelViewSet):
	queryset = Others.objects.all()
	serializer_class = OthersDetailSerializer
	permission_classes = (OthersPermission,)
	lookup_field = 'slug'

	def get_serializer_class(self):
		if self.action == 'list':
			return OthersListSerializer
		return OthersDetailSerializer

def project_redirect(request, *args, **kwargs):
	return HttpResponsePermanentRedirect("/api/others/project/")

def about_redirect(request, *args, **kwargs):
	return HttpResponsePermanentRedirect("/api/others/about/")
