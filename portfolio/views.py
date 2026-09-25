import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')

# @csrf_exempt
# @require_POST
def contact(request):
    # Normal page visit — show the contact form
    if request.method == 'GET':
        return render(request, 'portfolio/contact.html')

    # Form submission — expects a POST with JSON body
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid data.'}, status=400)

        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return JsonResponse({'error': 'Name, email and message are required.'}, status=400)

        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )

        send_mail(
            subject=f"Portfolio Contact: {subject or 'New message'} from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_RECEIVE_EMAIL],
            fail_silently=False,
        )

        return JsonResponse({'success': 'Message sent! I will get back to you soon.'})

    # Anything else (PUT, DELETE, etc.)
    return JsonResponse({'error': 'Method not allowed.'}, status=405)



def about(request):
    return render(request, 'portfolio/about.html')


def services(request):
    return render(request, 'portfolio/services.html')


def resume(request):
    return render (request, "portfolio/resume.html")


def view_my_work(request):
    return render(request, 'portfolio/view_my_work.html')


