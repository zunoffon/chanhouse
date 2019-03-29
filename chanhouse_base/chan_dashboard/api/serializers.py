from rest_framework import serializers
from ..models import BookDate


class BookDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDate
        fields = ['user', 'orderDate', 'status']
