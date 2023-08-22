from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import NewsCategoryListAPIViewSet, AreaCategoryListAPIViewSet, PostLIstAPIViewSet, UserListAPIViewSet

router = DefaultRouter()
router.register('news', NewsCategoryListAPIViewSet, basename='news')
router.register('area', AreaCategoryListAPIViewSet, basename='area')
router.register('posts', PostLIstAPIViewSet, basename='postr')
router.register('user', UserListAPIViewSet, basename='users')
# router.register('filters', PostProductList,basename='filters')
# router.register('filter/', IntroductionViewSet,basename='filter')

urlpatterns = [
    path('', include(router.urls)),
    # path('post1/', views.post, name="post1"),
]
