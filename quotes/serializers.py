from rest_framework import fields, serializers
from .models import Quote, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields=['tag']

class QuoteSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True)

    class Meta:
        model = Quote
        fields = ['id', 'frase', 'autor', 'tags']

