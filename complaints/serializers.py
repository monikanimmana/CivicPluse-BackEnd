from .models import *
from rest_framework import serializers

class complaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=Complaint
        fields=[
            'complaint_title',
            'complaint_description',
            'complaint_address',
            'complaint_category',
            'complaint_image',
            'complaint_priority',
            'longitude',
            'latitude',

        ]
        extra_kwargs = {
            'complaint_image': {'required': False, 'allow_null': True}
        }

class AssignOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Complaint
        fields=[
            'assignOfficer',
        ]