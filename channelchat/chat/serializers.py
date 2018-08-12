from rest_framework import serializers
from .models import channel, chat

class addChatSerializer(serializers.ModelSerializer):
	class Meta:
		model = chat
		fields = ['content','user','channel']