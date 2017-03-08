from rest_framework import serializers
from others.models import Others

class OthersListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Others
		fields = ('title', 'tag', 'slug', 'digest', 'time')

class OthersDetailSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Others
		fields = ('title', 'tag', 'slug', 'content', 'time')
