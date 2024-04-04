from django.db import models
from django.contrib.auth.models import User


class Attendance(models.Model):
    """Table to mark the attendance of staff"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True)
    hours= models.IntegerField(null=True)
    active_orders = models.IntegerField(default=0)
    def __str__(self):
        return str(self.user_id)