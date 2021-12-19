
from .serializers import  OrderSerializer
from .models import  Order


from django.http import HttpResponse
import requests
from django.shortcuts import render
import json  
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

import pandas as pd
from requests.auth import HTTPBasicAuth
import requests
import json


def error_404(request, exception):
    data = {}
    return render(request,'blog/error.html', data)

def home(request):
    data = Order.objects.all()
    return render(request, 'blog/base.html', {'data':data})