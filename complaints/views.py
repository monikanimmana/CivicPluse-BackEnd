from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import *
from .models import *
from .serializers import *
from django.utils.timezone import now
from rest_framework.views import APIView


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
    
class ComplaintDetails(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=complaintSerializer

    def get_queryset(self):
        return Complaint.objects.filter(created_by=self.request.user)
    

class DeleteComplaint(DestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=complaintSerializer

    def get_queryset(self):
        return Complaint.objects.filter(created_by=self.request.user)
    
class AssignOfficer(UpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AssignOfficeSerializer
    queryset=Complaint.objects.all()

    def perform_update(self, serializer):
        office=serializer.validated_data['assignedOfficer']
        if office.role!="officer" :
            raise ValidationError("selected user is not a officer")
        
        serializer.save(status="assigned")

class ListOfficerComplaints(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=complaintSerializer
    
    def get_queryset(self):
        return Complaint.objects.filter(assignedOfficer=self.request.user)
        
class UpdateComplaintStatus(UpdateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AssignOfficeSerializer

    def get_queryset(self):
        return Complaint.objects.filter(assignedOfficer=self.request.user)
        
    def perform_update(self,serializer):
        complaints=serializer.save()

        if complaints.complaint_status == "resolved":
            complaints.resolved_at=now()

        serializer.save()
         
class CitizenDashboard(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        complaints=Complaint.objects.filter(created_by=self.request.user)

        data = {
            
        }



    
