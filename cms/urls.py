from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet, blogList_redirect
from dairy.views import DairyViewSet, dairyList_redirect
from others.views import OthersViewSet, project_redirect, about_redirect
from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()

blog_list = BlogViewSet.as_view({
	'get': 'list'
	});

blog_detail = BlogViewSet.as_view({
	'get': 'retrieve'
	});

dairy_list = DairyViewSet.as_view({
	'get': 'list'
	});

dairy_detail = DairyViewSet.as_view({
	'get': 'retrieve'
	});

router.register(r'others', OthersViewSet)

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	url(r'^api/articleList/(?P<pk>[0-9]+)/$', blogList_redirect, name='blog-redirect'),
	url(r'^api/blogList/$', blog_list, name='blog-list'),
	url(r'^api/articles/(?P<pk>[0-9]+)/$', blog_detail, name='blog-detail'),

	url(r'^api/dairyList/(?P<pk>[0-9]+)/$', dairyList_redirect, name='dairy-redirect'),
	url(r'^api/dairylist/$', dairy_list, name='dairy-list'),
	url(r'^api/dairy/(?P<pk>[0-9]+)/$', dairy_detail, name='dairy-detail'),

	url(r'^api/project/$', project_redirect, name='project-redirect'),
	url(r'^api/about/$', about_redirect, name='about-redirect'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)