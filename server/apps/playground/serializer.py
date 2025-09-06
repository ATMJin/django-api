from rest_framework import serializers
from server.apps.playground.models import Item, ItemComment


class ItemCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemComment
        fields = (
            "id",
            "content",
            "created_at",
            "updated_at",
        )


class ItemSerializer(serializers.ModelSerializer):
    comments = ItemCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "description",
            "comments",
        )

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name field is required.")
        elif Item.objects.filter(name=value).exists():
            raise serializers.ValidationError("Item with this name already exists.")
        return value
