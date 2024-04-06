from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FileUploadSerializer
from .models import UploadedFile

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os
from django.http import Http404


class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    
    def get(self, request, *args, **kwargs):
        files = UploadedFile.objects.all()
        serializer = self.serializer_class(files, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def download_file(self, file_name):
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = f'inline; filename="{file_name}"'
                return response
        raise Http404

    def get(self, request, *args, **kwargs):
        if 'download' in request.query_params:
            file_name = request.query_params['download']
            return self.download_file(file_name)
        else:
            files = UploadedFile.objects.all()
            serializer = self.serializer_class(files, many=True)
            return Response(serializer.data)
