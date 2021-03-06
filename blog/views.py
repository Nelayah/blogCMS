from django.http import HttpResponsePermanentRedirect
from blog.models import Blog
from blog.serializers import BlogListSerializer, BlogDetailSerializer
from blog.permissions import BlogPermission
from rest_framework import viewsets
from rest_framework.response import Response

class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogDetailSerializer
	permission_classes = (BlogPermission,)
	lookup_field = 'pk'

	def get_serializer_class(self):
		if self.action == 'list':
			return BlogListSerializer
		return BlogDetailSerializer

def blogList_redirect(request, *args, **kwargs):
	offset = (int(kwargs['pk']) - 1) * 5
	return HttpResponsePermanentRedirect("/api/blogList/?limit=5&offset=" + str(offset))