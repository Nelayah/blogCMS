from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from blog.views import BlogViewSet
from dairy.views import DairyViewSet
from others.views import OthersViewSet
from django.contrib import admin
admin.autodiscover()

router = DefaultRouter()
router.register(r'blog', BlogViewSet)
router.register(r'dairy', DairyViewSet)
router.register(r'others', OthersViewSet)

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)