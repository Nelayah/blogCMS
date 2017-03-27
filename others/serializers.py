from rest_framework import serializers
from others.models import Others

class OthersListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Others
		fields = ('pk', 'title', 'tag', 'slug', 'digest', 'time')

class OthersDetailSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Others
		fields = ('pk', 'title', 'tag', 'slug', 'digest', 'content', 'time')
