from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response

from .serializers import NewsCategorySerializer, AreaCategorySerializer, PostSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import NewsCategory, AreaCategory, Post, User,Postlike
from .permission import NewsCategoryPermission, AreaCategoryPermission, PostPermissions, UserPermission

from rest_framework.filters import SearchFilter,OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class NewsCategoryListAPIViewSet(ModelViewSet):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects.all()
    permission_classes = (NewsCategoryPermission,)
    http_method_names = ['get', 'post']


class AreaCategoryListAPIViewSet(ModelViewSet):
    serializer_class = AreaCategorySerializer
    queryset = AreaCategory.objects.all()
    permission_classes = (AreaCategoryPermission,)
    http_method_names = ['get', 'post']


class PostLIstAPIViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (PostPermissions,)
    parser_classes = [MultiPartParser]

    filter_backends = (SearchFilter, )
    search_fields = ('title', 'text', 'to_author__username')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.method in SAFE_METHODS:
            instance.views += 1
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserListAPIViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (UserPermission,)


# Introduction visit


# class IntroductionViewSet(ModelViewSet):
#     serializer_class = IntroductionSerializer
#     queryset = Introduction.objects.all()
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterer_fields = ['id', 'name']
#     search_fields = ['=name', 'intro']
#     ordering_fields = ['name', 'id']
#     ordering = ['id']


# @api_view(["GET"])
# def allpost(request):
#     id = request.data
#     post_list = Post.objects.all()
#     like_count = Post.objects.filter(id=request.POST.get("pk")).count()
#     post_serializer = PostSerializer(post_list,many=True,context={"like_count":like_count})
#     return Response(request,post_serializer.data)
