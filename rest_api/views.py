from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
#class based views
from rest_framework.views import APIView
from django.http import Http404


# generic and mixins 
from rest_framework import generics
from rest_framework import mixins

#basic authentication
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#viewsets ->view sets come with generic,mixins and also with class based views
from rest_framework import viewsets




class PostViewSet(viewsets.GenericViewSet,
mixins.ListModelMixin,
mixins.CreateModelMixin,
mixins.DestroyModelMixin,
mixins.RetrieveModelMixin,
mixins.UpdateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()









# class PostViewSet(viewsets.ViewSet):

#     def list(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many =True)
#         return Response(serializer.data)
#     def create(self,request):
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
#     def update(self,request):
#         pass














# class genericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
#     lookup_field = 'id'     
#     #this is basic authentication for token based authentication we need to install the app
#     # authentication_classes = [SessionAuthentication,BasicAuthentication]
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     #
#     def get(self,request,id):
#         if id:
#             return self.retrieve(request)
#         else:                               #means id = 0
#             return self.list(request)

#     def post(self,request):
#         return self.create(request)
#     def put(self,request,id = None):
#         return self.update(request,id)
#     def delete(self,request,id = None):
#         return self.destroy(request,id)
    



















# Create your views here.
# class PostAPIView(APIView):
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many =True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)

# class postDetailAPIViews(APIView):
#     def get_object(self,id):
#         try:
#             return Post.objects.get(id = id)       
#         except Post.DoesNotExist:
#             raise Http404  
#     def get(self,request,id):
#         post = self.get_object(id)
#         # post = Post.objects.get(id = id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     def put(self,request,id):
#         post = self.get_object(id)
#         serializer = PostSerializer(post,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,id):
#         post = self.get_object(id)
#         post.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
































#FUCTIONS BASED VIEWS

# @api_view(['GET','POST'])
# def Posts(request):
#     if request.method == 'GET':
#         posts  = Post.objects.all()
#         serializer = PostSerializer(posts,many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':   
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status =status.HTTP_201_CREATED)
#         return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)




# @api_view(['GET','PUT','PATCH','DELETE'])
# def posts_detail(request,id):

#     try:
#         post = Post.objects.get(id = id)       
#     except post.DoesNotExist:
#         return Response(status = 404)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
    
#         serializer = PostSerializer(post,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)
        





        










