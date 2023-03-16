from rest_framework import serializers
from .models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(),
                                                read_only=True)

    class Meta:
        model = Message
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Chat
        fields = '__all__'
        # read_only_fields = ('owner',)


class DetailChatSerializer(ChatSerializer):
    messages = MessageSerializer(read_only=True, many=True)

    # read_only_fields = ['owner']
# class AttachmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attachment
#         fields = "__all__"

#     file_owner = serializers.HiddenField(
#         default=serializers.CurrentUserDefault())
