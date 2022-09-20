from django.urls import path
from .views import CategoriesLV, CategoriesDV, CategoriesCV

app_name = 'bookmark'

urlpatterns = [
    path('categories/', CategoriesLV.as_view(), name='categories'),
    path('category/<int:pk>/', CategoriesDV.as_view(), name='category_detail'),
    path('category/create/', CategoriesCV.as_view(), name='category_creat'),
]
