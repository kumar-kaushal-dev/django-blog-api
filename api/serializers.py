from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    """
    Serializer for the BlogPost model.
    Handles conversion between BlogPost instances and JSON representations.
    """

    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]
        read_only_fields = ["id", "published_date"]  # Prevent changes from the API

    def validate_title(self, value):
        """
        Custom validator to ensure title is not too short.
        """
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value
