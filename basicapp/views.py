from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer, CommentOnlySerializer, UserSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    urls = {
        '/api/posts/' : 'creating a post and listing all posts',
        '/api/posts/detail/<str:pk>/' : 'update and delete an existing post',
        '/api/posts/comments/<str:pk>/' : 'creating comment on a post and getting all comments on a post',
        '/api/users/' : 'creating an user and listing all users',
        '/api/users/<str:pk>/' : 'update an existing user'

    }

    return Response(urls)

# listing all posts and creating a post
class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        print('serializer data : ',serializer.data)

        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)


# class CommentView(APIView):
#     #adding comment to a post 
#     def post(self, request):
#         serializer = CommentSerializer(data=request.data)
#         print(request.data[''])
        

#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.data)
        
#         return Response(serializer.data)
    
#     def get(self, request):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)

#         return Response(serializer.data)

# class PostDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(id=pk)
#         except:
#             return Response('Object not found!!')
    
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         comments = post.comments.all()
#         serializer = CommentSerializer(comments,many=True)

#         return Response(serializer.data)



class CommentAddToPost(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except:
            return Response('Object not found!!')
    #getting all comments of a post
    def get(self, request, pk):
        post = self.get_object(pk)
        comments = post.comments.all()
        serializer = CommentSerializer(comments,many=True)

        return Response(serializer.data)

    #creating comments on a post
    def post(self, request, pk):
        
        post1 = self.get_object(pk)

        serializer = CommentOnlySerializer(data=request.data)
        print('requested data : ', request.data)

        if serializer.is_valid():
            
            serializer.save(post=post1)
            print('serilizer data :', serializer.data)
        
        return Response(serializer.data)
    

class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except:
            return Response('Object not found!!')
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        print(serializer.data)

        return Response(serializer.data)
    
    # update an existing post 
    def put(self, request, pk):
        post = self.get_object(pk)

        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    # delete an existing post
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()

        return Response("Object deleted!!")

class UserView(APIView):
    
    #creating a user
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    #listing all users
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class UpdateUserView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except:
            return Response('User not found!!')

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    


