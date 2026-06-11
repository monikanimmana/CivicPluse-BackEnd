from django.urls import path
from .views import *

urlpatterns =[
    path('create/',CreateComplaint.as_view(),name='create_complaint'),
    path('my/',MyComplaint.as_view(),name='my_complaint'),
    path('updatecomplaint/<int:pk>/',UpdateComplaint.as_view(),name='update_complaint'),
    path('details/<int:pk>',ComplaintDetails.as_view(),name='complaint_deatils'),
    path('delete/',DeleteComplaint.as_view(),name='delete_complaint'),
]