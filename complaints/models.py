from django.db import models
from users.models import User

# Create your models here.
class Complaint(models.Model):
      CATEGORY_CHOICES = (
            ('road','road'),
            ('water','water'),
            ('electricity','electricity'),
            ('sanitation','sanitation'),
      )

      STATUS_CHOICES=(
            ('pending','pending'),
            ('in_progess','in_process'),
            ('assigned','assigned'),
            ('solved','solved'),
            ('closed','closed'),
      )

      PRIORITY_CHOICES=(
            ('low','low'),
            ('medium','medium'),
            ('high','high'),
            ('emergency','emergency'),
      )

      complaint_iD=models.CharField(max_length=50,unique=True,blank=True)
      complaint_title=models.CharField(max_length=100)
      complaint_description=models.TextField()
      complaint_address=models.CharField(max_length=50)
      complaint_category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default='road')
      complaint_image=models.ImageField(upload_to='complaint_images/',null=True,blank=True)
      latitude=models.DecimalField(max_digits=10,decimal_places=7)
      longitude=models.DecimalField(max_digits=10,decimal_places=7)
      complaint_status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
      complaint_priority=models.CharField(max_length=20,choices=PRIORITY_CHOICES,default='medum')
      created_by=models.ForeignKey(User , on_delete=models.CASCADE , related_name='complaints_created')
      assignedOfficer=models.ForeignKey(User , on_delete=models.SET_NULL,null=True,blank=True,related_name='complaints_assigned')
      created_at=models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)

      def __str__(self):
            return f"{self.complaint_title} ({self.complaint_status})"










