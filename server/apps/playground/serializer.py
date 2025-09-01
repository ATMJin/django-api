from rest_framework import serializers
from server.apps.playground.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "description",
        )

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name field is required.")
        elif Item.objects.filter(name=value).exists():
            raise serializers.ValidationError("Item with this name already exists.")
        return value
