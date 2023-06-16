from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

# Create your views here.

from . serilizers import *


class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        try:
            serializer = FileListSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
    
    # def post(self, request, format=None):

    #     try: 
    #         serializer = FileListSerializer(data = request.data)

    #         if serializer.is_valid():
    #             serializer.save()

    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     except Exception as e:
    #         print(e)

