from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import JobPost, Application
from .serializers import JobPostSerializer, ApplicationSerializer
# Create your views here.

class JobPostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        job_posts = JobPost.objects.filter(hr=request.user)
        serializer = JobPostSerializer(job_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hr=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class ApplicationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, job_post_id):
        job_post = JobPost.objects.get(id=job_post_id)
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(job_post=job_post, job_seeker=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
