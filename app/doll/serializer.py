from rest_framework import serializers

from .models import Doll


class DollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doll
        fields = (
            'id',
            'code_name',
            'rank',
            'type',
            'image',
        )
