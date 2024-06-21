from django.shortcuts import render, redirect
from ..models import CustomerFeedback
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def feedback_view(request):
    if request.method == 'POST':
        
        # request_number = request.POST.get('request_number')
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        email_id = request.POST.get('email_id')
        problem_resolution_time = request.POST.get('problem_resolution_time')
        timely_update_information = request.POST.get('timely_update_information')
        technical_skill_service_engineer = request.POST.get('technical_skill_service_engineer')
        communication_attire_behavior = request.POST.get('communication_attire_behavior')
        response_backend_team = request.POST.get('response_backend_team')
        overall_experience = request.POST.get('overall_experience')
        suggestions = request.POST.get('suggestions')

        feedback = CustomerFeedback(
            # request_number=request_number,
            name=name,
            mobile_number=mobile_number,
            email_id=email_id,
            problem_resolution_time=problem_resolution_time,
            timely_update_information=timely_update_information,
            technical_skill_service_engineer=technical_skill_service_engineer,
            communication_attire_behavior=communication_attire_behavior,
            response_backend_team=response_backend_team,
            overall_experience=overall_experience,
            suggestions=suggestions
        )
        feedback.save()
        return redirect('feedback_thank_you')
    return render(request, 'feedback/feedback_form.html')

def feedback_thank_you(request):
    return render(request, 'feedback/thank_you.html')
