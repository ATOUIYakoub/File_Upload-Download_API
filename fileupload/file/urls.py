from django.urls import path
from .views import FileUploadAPIView

app_name = 'file'

urlpatterns = [
    path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),
    path('download-file/', FileUploadAPIView.as_view(), name='download-file'),
]
