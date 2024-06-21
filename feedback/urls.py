from django.urls import path
from .feedback_views.feedback import feedback_view, feedback_thank_you

urlpatterns = [
    path('', feedback_view, name='feedback_form'),
    path('feedback/thank-you/', feedback_thank_you, name='feedback_thank_you'),
]
