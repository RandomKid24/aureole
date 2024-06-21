from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

class CustomerFeedback(models.Model):
    request_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,null=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField()

    PROBLEM_RESOLUTION_CHOICES = [    (5, 'Excellent / Appreciable'),    (4, 'Very Good / More than expectations'),    (3, 'Good / As expected'),    (2, 'Poor / Below average or below than expectations'),    (1, 'Very Poor / Needed improvement')]

    problem_resolution_time = models.IntegerField(choices=PROBLEM_RESOLUTION_CHOICES)
    timely_update_information = models.IntegerField(choices=PROBLEM_RESOLUTION_CHOICES)
    technical_skill_service_engineer = models.IntegerField(choices=PROBLEM_RESOLUTION_CHOICES)
    communication_attire_behavior = models.IntegerField(choices=PROBLEM_RESOLUTION_CHOICES)
    response_backend_team = models.IntegerField(choices=PROBLEM_RESOLUTION_CHOICES)
    overall_experience = models.IntegerField(choices=PROBLEM_RESOLUTION_CHOICES)

    # Additional Feedback
    suggestions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.email_id})"
    
class Verify(models.Model):
    email = models.EmailField(("Email"), max_length=254)
    otp = models.CharField(("OTP"), max_length=50)