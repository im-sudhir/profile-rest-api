from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

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