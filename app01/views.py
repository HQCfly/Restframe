from django.shortcuts import render,HttpResponse

# Create your views here.

from django.views import View
from rest_framework.response import Response
from .models import *

from app01.serilizer import *


from rest_framework.views import APIView
class PublishView(APIView):
    def get(self,request):

        # restframework
        # 取数据
        # print("request.data", request.data)
        # print("request.data type", type(request.data))
        # print(request._request.GET)
        # print(request.GET)
        # 序列化
        # 方式1：
        # publish_list=list(Publish.objects.all().values("name","email"))

        # 方式2：
        # from django.forms.models import model_to_dict
        # publish_list=Publish.objects.all()
        # temp=[]
        # for obj in publish_list:
        #     temp.append(model_to_dict(obj))

        # 方式3：
        # from django.core import serializers
        # ret=serializers.serialize("json",publish_list)

        # 序列组件
        publish_list = Publish.objects.all()
        ps = PublishModelSerializers(publish_list, many=True)
        return Response(ps.data)

    def post(self,request):
        # 取数据
        # 原生request支持的操作
        # print("POST",request.POST)
        # print("body",request.body)
        # # print(request)
        # print(type(request))
        # from django.core.handlers.wsgi import WSGIRequest
        #  新的request支持的操作
        # print("request.data",request.data)
        # print("request.data type",type(request.data))


        #
        # post请求的数据
        ps = PublishModelSerializers(data=request.data)
        if ps.is_valid():
            print(ps.validated_data)
            ps.save()  # create方法
            return Response(ps.data)
        else:
            return Response(ps.errors)


class PublishDetailView(APIView):
    def get(self, request, pk):

        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish)
        return Response(ps.data)

    def put(self, request, pk):
        publish = Publish.objects.filter(pk=pk).first()
        ps = PublishModelSerializers(publish, data=request.data)
        if ps.is_valid():
            ps.save()
            return Response(ps.data)
        else:
            return Response(ps.errors)

    def delete(self, request, pk):
        Publish.objects.filter(pk=pk).delete()

        return Response()


class BookView(APIView):
    def get(self,request):
        book_list=Book.objects.all()
        bs=BookModelSerializers(book_list,many=True,context={'request': request})
        return Response(bs.data)
    def post(self,request):
        # post请求的数据
        bs=BookModelSerializers(data=request.data)
        if bs.is_valid():
            print(bs.validated_data)
            bs.save()# create方法
            return Response(bs.data)
        else:
            return Response(bs.errors)

class BookDetailView(APIView):

    def get(self,request,id):

        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,context={'request': request})
        return Response(bs.data)

    def put(self,request,id):
        book=Book.objects.filter(pk=id).first()
        bs=BookModelSerializers(book,data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        else:
            return Response(bs.errors)

    def delete(self,request,id):
        Book.objects.filter(pk=id).delete()

        return Response()