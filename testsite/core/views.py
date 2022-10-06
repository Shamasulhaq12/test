from rest_framework.views import APIView
from django.http import Http404
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class RegisterView(APIView):
    serializer_class   = UserSerializer
    permission_classes = [AllowAny,]
    
    def post(self, request, format=None):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            name=serializer.data['name']
           
            return Response([{"Welcome dear  {} ".format(name)}, ], status=201)
        except Exception as e:
            print(e)
            return Response([{"user": "not found"}, ], status=404)
        
       