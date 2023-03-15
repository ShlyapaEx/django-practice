from rest_framework import serializers
from .models import Attachment, Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Chat
        fields = '__all__'

        # read_only_fields = ['owner']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                                read_only=True)

    def create(self, validated_data):
        validated_data['sender'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = Message
        fields = "__all__"


# class AttachmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attachment
#         fields = "__all__"

#     file_owner = serializers.HiddenField(
#         default=serializers.CurrentUserDefault())
