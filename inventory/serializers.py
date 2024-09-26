from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    def validate_name(self, value):
        if Item.objects.filter(name=value).exists():
            raise serializers.ValidationError("Item already exists.")
        return value