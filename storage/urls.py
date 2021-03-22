from django.urls import include, path
from .views import UploadFileAPIView

urlpatterns = [
    path("file", UploadFileAPIView.as_view()),
]