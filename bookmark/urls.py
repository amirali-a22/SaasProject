from django.urls import path, include
from .views import CategoriesLV, CategoriesDV, CategoriesCV, BookmarksCV, BookmarksLV, BookmarksDV, CategoriesUV, \
    CategoriesDelete, BookmarksUV, BookmarksDelete

app_name = 'bookmark'

urlpatterns = [
    path('api/', include('bookmark.api.urls')),

    path('categories/', CategoriesLV.as_view(), name='categories'),
    path('category/detail/<int:pk>/', CategoriesDV.as_view(), name='category_detail'),
    path('category/edit/<int:pk>/', CategoriesUV.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', CategoriesDelete.as_view(), name='category_delete'),
    path('category/create/', CategoriesCV.as_view(), name='category_creat'),

    path('bookmarks/', BookmarksLV.as_view(), name='bookmarks'),
    path('bookmark/<int:pk>/', BookmarksDV.as_view(), name='bookmark_detail'),
    path('<int:category_id>/bookmark/create/', BookmarksCV.as_view(), name='bookmark_creat'),
    path('<int:category_id>/bookmark/edit/<int:pk>/', BookmarksUV.as_view(), name='bookmark_edit'),
    path('<int:category_id>/bookmark/delete/<int:pk>/', BookmarksDelete.as_view(), name='bookmark_delete'),

]
