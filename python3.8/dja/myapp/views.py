from django.shortcuts import render,HttpResponse,redirect,reverse
from django.db.models import Q,F
from myapp.serializers import *
from myapp import models
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import pagination                #分页
import datetime
import os
from dja import settings

# Create your views here.

class HelloWorldViewSet(GenericViewSet):
    """hello"""
    @action(detail=False)
    def verify(self,request):
        mes={'code':200}
        return Response(mes)

    @action(methods=["POST"],detail=False)
    def login(self, request, *args, **kwargs):
        mes={}
        name=request.data.get('name')
        password=request.data.get('password')
        res=models.Employee.objects.filter(Q(name=name),Q(password=password))
        print(res)
        print(name)
        print(password)
        mes={'code':200} if res else {'code':0}
        return Response(mes)
