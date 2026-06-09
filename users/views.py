from django.shortcuts import render
from rest_framework import generics , status
from .models import User
from .serializers import RegisterSerializer , LoginSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

class LoginView(APIView):

    def post(self , request):
        serializer = LoginSerializer(data = request.data)

        if(serializer.is_valid()):
            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh":str(refresh),
                    "access" : str(refresh.access_token),
                    "username":user.username,
                    "role":user.role,
                }
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):

        return Response(
            {
                "id":request.user.id,
                "username":request.user.username,
                "email":request.user.email,
                "phone_no":request.user.phone_no,
                "role":request.user.role,
                "preferred_language":request.user.preferred_language,
            }
        )