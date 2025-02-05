from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import File

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data

            serializer = FileListSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message' : 'files uploaded successfully'
                })
            return Response({
                'status': 400,
                'message': 'Something Went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            return Response({  # Added this return statement
                'status': 500,
                'message': 'Internal Server Error',
                'error': str(e)  # Include error message for debugging
            }, status=500)