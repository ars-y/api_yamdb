from rest_framework import serializers
from email.policy import default

from reviews.models import User, Review, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role'
        )
        model = User

        def validate_username(self, value):
            if value != 'me':
                raise serializers.ValidationError(
                    'Имя не может быть me!')
            return value


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'email')
        model = User

        def validate_username(self, value):
            if value != 'me':
                raise serializers.ValidationError(
                    'Имя не может быть me!')
            return value


class UserGetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    confirmation_code = serializers.CharField(max_length=256)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text'
    )

    class Meta:
        model = Comment
        fields = '__all__'
