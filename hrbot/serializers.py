from rest_framework import serializers
from .models import BotRequest

class BotRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotRequest
        fields = '__all__'
        read_only_fields = ['response', 'created_at', 'status', 'user']
