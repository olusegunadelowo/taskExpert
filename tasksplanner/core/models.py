from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.
class Taskn(models.Model):                      #Task class inherits from models.Model, which is the base class for all Django models. This allows us to define the structure of our Task model and interact with the database using Django's ORM (Object-Relational Mapping).
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField(default=timezone.now) #to set startime as now
    end_time = models.DateTimeField(blank=True, null=True) #To avoid validation errors when start_time is not provided, we set blank=True and null=True. This allows the field to be optional in forms and the database.
    done = models.BooleanField(default=False)
   
    @property
    def is_expired(self):
        local_now = timezone.now()  # Get the current local time with timezone information
        print(local_now, self.end_time)
        if self.end_time and self.end_time < local_now:
            return True
        return False

