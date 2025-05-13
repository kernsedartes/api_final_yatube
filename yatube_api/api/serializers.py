from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer, TokenVerifySerializer
)
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from posts.models import Comment, Post, Group, Follow, User


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except TokenError:
            raise InvalidToken({
                'detail': 'Token is invalid or expired',
                'code': 'token_not_valid'
            })


class CustomTokenVerifySerializer(TokenVerifySerializer):
    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except TokenError:
            raise InvalidToken({
                'detail': 'Token is invalid or expired',
                'code': 'token_not_valid'
            })


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True, read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    follower = serializers.StringRelatedField(many=True, read_only=True)
    following = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'posts',
            'comments',
            'follower',
            'following',
        )
        ref_name = 'ReadOnlyUsers'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    group = serializers.PrimaryKeyRelatedField(
        queryset=Group.objects.all(), required=False, allow_null=True
    )
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны на этого пользователя'
            )
        ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return value
