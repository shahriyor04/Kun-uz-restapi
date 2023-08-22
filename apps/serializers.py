from rest_framework.fields import HiddenField, CurrentUserDefault

from .models import NewsCategory, AreaCategory, Post, User, Postlike
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class NewsCategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"


class AreaCategorySerializer(ModelSerializer):
    class Meta:
        model = AreaCategory
        fields = "__all__"


class PostSerializer(ModelSerializer):
    to_author = HiddenField(default=CurrentUserDefault())
    like = SerializerMethodField('like_count')

    class Meta:
        model = Post
        fields = "__all__"

    def like_count(self, obj):
        total_like = Postlike.objects.filter(id=obj.id).count()
        return total_like

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['category'] = AreaCategory(instance.to_AreaCategory)
    #     return data

#
# # Introduction Serializer
#
# class IntroductionSerializer(ModelSerializer):
#     class Meta:
#         model = Introduction
#         fields = "__all__"
