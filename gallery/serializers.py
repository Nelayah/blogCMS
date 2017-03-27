from rest_framework import serializers
from gallery.models import Gallery

class GallerySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Gallery
		fields = ('title', 'images', 'time')
