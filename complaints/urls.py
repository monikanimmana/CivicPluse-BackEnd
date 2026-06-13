from django.urls import path
from .views import *

urlpatterns =[
    path('create/',CreateComplaint.as_view(),name='create_complaint'),
    path('my/',MyComplaint.as_view(),name='my_complaint'),
    path('updatecomplaint/<int:pk>/',UpdateComplaint.as_view(),name='update_complaint'),
    path('details/<int:pk>',ComplaintDetails.as_view(),name='complaint_deatils'),
    path('delete/',DeleteComplaint.as_view(),name='delete_complaint'),
    path('assign-officer/<int:pk>',AssignOfficer.as_view(),name="assign_officer"),
    path('officer-complaints/',ListOfficerComplaints.as_view(),name="officer_complaints"),
    path('updatecomplaint_status/',UpdateComplaintStatus.as_view(),name="complaint_status"),
    
]