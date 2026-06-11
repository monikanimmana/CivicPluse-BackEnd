from django.shortcuts import render
from rest_framework.generics import CreateAPIView ,ListAPIView ,UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.
class CreateComplaint(CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Complaint.objects.all()
    serializer_class=complaintSerializer

    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)

class MyComplaint(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=complaintSerializer

    def get_queryset(self):
        return Complaint.objects.filter(created_by=self.request.user)

class UpdateComplaint(UpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=complaintSerializer

    def get_queryset(self):
        return Complaint.objects.filter(created_by=self.request.user)

    

    
