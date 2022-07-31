from dataclasses import fields
from rest_framework import serializers
from .models import Attachment, Chat, Message
from django.core.files.uploadedfile import InMemoryUploadedFile


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
        read_only_fields = ['owner']

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = "__all__"

    file_owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault())


class MessageSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        attachments = kwargs.pop('attachments', None)
        super().__init__(*args, **kwargs)
        if attachments:
            attachments_update_dict = {field: serializers.FileField(
                required=False, write_only=True) for field in attachments}
            self.fields.update(**attachments_update_dict)

    def create(self, validated_data):
        validated_data_copy = validated_data.copy()
        validated_files = []
        for key, value in validated_data_copy.items():
            if isinstance(value, InMemoryUploadedFile):
                validated_files.append(value)
                validated_data.pop(key)
        message_instance = super().create(validated_data)
        for file in validated_files:
            Attachment.objects.create(
                message=message_instance, file=file, file_owner=validated_data.get('chat').owner)
        return message_instance

    class Meta:
        model = Message
        fields = "__all__"

    sender = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True)
    # attachments = AttachmentSerializer(many=True)
