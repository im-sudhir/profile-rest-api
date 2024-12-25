from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer,UserProfileSerializer, ProfileFeedItemSerializer
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions
from rest_framework.permissions import IsAuthenticated


class HelloApiView(APIView):
    """Test API View"""
    serializer_class=HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView Features"""
        an_apiview=[
           'Uses HTTP methodsas function (get, post, put, patch, delete)',
           'Is similar to a traditional Django View',
           'Gives you the most conrol over your application logic',
           'Is mapped manually to URL',
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})


    def post(self, request, format=None):
        """creates a hello method with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            return Response({'message': f'Hello {name}'})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    
    def patch(self,request,pk=None):
        """Handle partial update of an object"""
        return Response({'method':'PATCH'})

    
    def delete(self,request, pk=None):

        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class=HelloSerializer
    
    def list(self,request):
        """Return a Hello message"""
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_update, destory)',
            'Automatically maps to urls using routers',
            'provides more funcationality with less code',
        ]
        return Response({'message':"Hello",'a_viewset' : a_viewset})
    

    def create(self,request):
        """Create a new hello message"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello{name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """Handle getting an object by its Id"""
        return Response({'http_method':"GET"})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'http_method':"PATCH"})
    
    def destory(self,request,pk=None):
        """Handle deletion of an object"""
        return Response({'http_method':"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class= UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes= (permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewset(viewsets.ModelViewSet):
    """Handles creating and reading and updating profile feed itesm."""
    authentication_classes=(TokenAuthentication,)
    serializer_class= ProfileFeedItemSerializer
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(permissions.UpdateOwnStatus, IsAuthenticated)


    def perform_create(self,serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
