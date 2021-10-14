from django.shortcuts import get_list_or_404
from django.db.models import Q
from rest_framework import viewsets, generics
from .models import Topic, Document, Folder
from .serializers import TopicSerializer, DocumentSerializer, FolderSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Topics to be viewed or edited.
    """
    queryset = Topic.objects.all().order_by('name')
    serializer_class = TopicSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Documents to be viewed or edited.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class FolderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Folders to be viewed or edited.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class DocumentsByTagViewSet(generics.ListAPIView):
    """
    View-only API endpoint that allows Documents to be
    queried by topic or Topic and Folder.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = ('topic', 'folder')

    def get_queryset(self):
        topic = self.kwargs.get('topic')
        folder = self.kwargs.get('folder')
        if topic and folder:
            queryset = Document.objects.filter(
                Q(topic__name=topic) & Q(folder__name=folder)
            )
            get_list_or_404(queryset)
            return queryset
        if topic:
            queryset = Document.objects.filter(topic__name=topic)
            get_list_or_404(queryset)
            return queryset
