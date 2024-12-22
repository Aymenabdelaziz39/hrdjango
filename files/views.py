from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import UploadedFile
# Create your views here.
class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES['file']
        uploaded_file = UploadedFile.objects.create(user=request.user, file=file)
        return Response({"file_url": uploaded_file.file.url})
