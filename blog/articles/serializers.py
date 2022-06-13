from rest_framework import serializers
from .models import Articles, CustomUser
from django.contrib.auth import password_validation


class ArticlesRegistrSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2')

    def validate(self, data):
        password_validation.validate_password(data['password'])
        return data

    def save(self, *args, **kwargs):
        user = CustomUser(
            email=self.validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user


class ArticlesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'author', 'title', 'date', 'public')


class ArticlesDetailSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Articles
        fields = '__all__'


class ArticlesPrivateListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'author', 'title', 'date', 'public')
