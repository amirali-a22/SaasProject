from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import BookmarkSerializer, CategorySerializer
from ..models import Category, Bookmark


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    # permission_classes = [permissions.IsAuthenticated]
    @action(detail=True, methods=['post'], url_path='increase')
    def increase_visit_count(self, request, pk=None):
        try:
            self.get_object().increase_visit_count()
            return Response({'status': 'ok'})
        except Exception as e:
            return Response({'response': e}, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
