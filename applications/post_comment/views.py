from django.shortcuts import render
from rest_framework import viewsets
from .models import Data
from .serializers import CommentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from bson import json_util, ObjectId
import json

# Create your views here.
from django.http import JsonResponse
@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

    	return JsonResponse(Data.data,safe=False)
