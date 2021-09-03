from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views


router = DefaultRouter()
router.register('article', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
