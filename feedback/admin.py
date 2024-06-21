from django.contrib import admin
from .models import CustomerFeedback

@admin.register(CustomerFeedback)
class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('request_number','name', 'email_id', 'overall_experience')
    search_fields = ('name', 'email_id', 'mobile_number')
    list_filter = ('overall_experience',)
