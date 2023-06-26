from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactUsDetails, Registration, Donation

@csrf_exempt
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Create ContactUsDetails object
        contact_details = ContactUsDetails(name=name, email=email, phone=phone, message=message)
        contact_details.save()

        return JsonResponse({'message': 'Contact details received successfully.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        experience = request.POST.get('experience')

        # Create Registration object
        registration = Registration(name=name, email=email, phone=phone, address=address, dob=dob, experience=experience)
        registration.save()

        return JsonResponse({'message': 'Registration successful.'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)


@csrf_exempt
def donation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pin_code = request.POST.get('pin_code')
        purpose = request.POST.get('purpose')

        # Create Donation object
        donation = Donation(name=name, amount=amount, phone=phone, email=email, address=address, pin_code=pin_code, purpose=purpose)
        donation.save()

        return JsonResponse({'message': 'Donation received. Thank you!'})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
