from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "published_date",
            "created_at",
            "days_since_created",
        ]

    def get_days_since_created(self, obj):
        # from datetime import datetime, timezone
        # The above works only if created_at is DateTimeField then you
        # use return (datetime.now(timezone.utc) - obj.created_at).days
        from datetime import date, timezone

        return (date.today() - obj.created_at).days
