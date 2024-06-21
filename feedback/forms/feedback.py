from django import forms
from ..models import CustomerFeedback

class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = [
            'name', 'email_id', 'mobile_number', 'request_number',
            'problem_resolution_time', 'timely_update_information', 
            'technical_skill_service_engineer', 'communication_attire_behavior',
            'response_backend_team', 'overall_experience', 'suggestions'
        ]
        widgets = {
            'problem_resolution_time': forms.RadioSelect,
            'timely_update_information': forms.RadioSelect,
            'technical_skill_service_engineer': forms.RadioSelect,
            'communication_attire_behavior': forms.RadioSelect,
            'response_backend_team': forms.RadioSelect,
            'overall_experience': forms.RadioSelect,
        }
