from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLES_CHOICE=(
        ('citizen','Citizen'),
        ('worker','Worker'),
        ('officer','Officer'),
        ('admin','Admin'),
    )

    role = models.CharField(max_length=10,choices=ROLES_CHOICE,default='citizen')
    phone_no=models.CharField(max_length=15,null=True,blank=True,unique=True)
    preferred_language=models.CharField(max_length=12,default='English')
    profile=models.ImageField(upload_to='profiles/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    



    

