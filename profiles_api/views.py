from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView Features"""
        an_apiview=[
           'Uses HTTP methodsas function (get, post, put, patch, delete)',
           'Is similar to a traditional Django View',
           'Gives you the most conrol over your application logic',
           'Is mapped manually to URL',
        ]
        return Response({'message':'Hello', 'an_apiview': an_apiview})
