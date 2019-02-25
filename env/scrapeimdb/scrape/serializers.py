from rest_framework import serializers

from .models import Movie, Role


class RoleSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Role.objects.create(**validated_data)

    class Meta:
        model = Role
        fields = ('name', 'character')


class MovieSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        data = validated_data.pop('roles')
        cast = Movie.objects.create(**validated_data)
        for data in data:
            Role.objects.create(cast=cast, **data)
        return cast

    class Meta:
        model = Movie
        fields = (
                  'owner', 'movie_name', 'movie_star', 'movie_description', 'movie_pic', 'roles')
