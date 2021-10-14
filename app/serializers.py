from .models import Topic, Document, Folder
from rest_framework import serializers


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes all fields for the Topic Model and displays a HyperLink
    """
    class Meta:
        model = Topic
        fields = '__all__'


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes all fields for the Document Model and displays a HyperLink
    """
    class Meta:
        model = Document
        fields = '__all__'


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes all fields for the Folder Model and displays a HyperLink
    """
    class Meta:
        model = Folder
        fields = '__all__'
