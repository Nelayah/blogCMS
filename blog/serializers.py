from rest_framework import serializers
from blog.models import Blog

class BlogListSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Blog
		fields = ('pk', 'title', 'tag', 'slug', 'digest', 'time')

class BlogDetailSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Blog
		fields = ('pk', 'title', 'tag', 'slug', 'digest', 'content', 'time')
