from rest_framework import serializers
from .models import Search

class TapSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ['word', 'paragraph']