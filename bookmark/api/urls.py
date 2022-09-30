from django.urls import include, path
from rest_framework import routers
from .views import CategoryViewSet, BookmarkViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'bookmark', BookmarkViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
