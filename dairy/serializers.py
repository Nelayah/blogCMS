from rest_framework import serializers
from dairy.models import Dairy

class DairyListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Dairy
		fields = ('title', 'tag', 'slug', 'digest', 'time')

class DairyDetailSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Dairy
		fields = ('title', 'tag', 'slug', 'content', 'time')
