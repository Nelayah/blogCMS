from blog.models import Blog
from blog.serializers import BlogListSerializer, BlogDetailSerializer
from blog.permissions import BlogPermission
from rest_framework import viewsets
from rest_framework.response import Response

class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogDetailSerializer
	permission_classes = (BlogPermission,)
	lookup_field = 'slug'

	def get_serializer_class(self):
		if self.action == 'list':
			return BlogListSerializer
		return BlogDetailSerializer
