from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    published_year = serializers.IntegerField(read_only=True)
    author = serializers.CharField(required=False, allow_blank=True, max_length=100)
    genre = serializers.CharField(required=False, allow_blank=True, max_length=100)
    rating = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)



class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'username', 'books', 'owner']