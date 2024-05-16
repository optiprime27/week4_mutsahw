from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):
    agreeRate = serializers.SerializerMethodField()
    disagreeRate = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'agree', 'disagree', 'agreeRate', 'disagreeRate', 'createdAt']

    def get_agreeRate(self, obj):
        return obj.agree_rate()
        
    def get_disagreeRate(self, obj):
        return obj.disagree_rate()

class TopicRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('title', 'description')