from django.db import models


# Create your models here.
class Department(models.Model):
   dept_id=models.CharField(max_length=10)
   dept_name=models.CharField(max_length=20)
   dept_description=models.TextField()
   is_active=models.BooleanField(default=True)

   def __str__(self):
      return f"{self.dept_name} ({self.is_active})"
    