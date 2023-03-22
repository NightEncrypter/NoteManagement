from django.shortcuts import render
from rest_framework.response import Response

from accounts.models import Comment
# Create your views here.

def comment(request):
    
    
    # serializer=Comment(data)
    return Response()