from dairy.models import Dairy
from dairy.serializers import DairyListSerializer, DairyDetailSerializer
from dairy.permissions import DairyPermission
from rest_framework import viewsets
from rest_framework.response import Response

class DairyViewSet(viewsets.ModelViewSet):
	queryset = Dairy.objects.all()
	serializer_class = DairyDetailSerializer
	permission_classes = (DairyPermission,)
	lookup_field = 'slug'

	def get_serializer_class(self):
		if self.action == 'list':
			return DairyListSerializer
		return DairyDetailSerializer
