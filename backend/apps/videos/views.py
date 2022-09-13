from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serealizers import VideoSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

