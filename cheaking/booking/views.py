from django.shortcuts import render 
from django.conf import settings
from twilio.rest import Client as TwilioClient
from booking.models import Plumber
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

# def bookings(request):
#     return render(request,"booking.html")

def submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        service = request.POST.get('service')
        message = request.POST.get('message')

        abc= Plumber(Name=name,Phone=phone,Location=location,Service=service,message=message)
        abc.save()
        book = Plumber.objects.create(Name=name,Phone=phone,Location=location,Service=service,message=message)
        send_whatsapp(book)
    return render(request,"submit.html")


def send_whatsapp(book):
    client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message_body = (
        f"New booking from ' {book.Name} '.\n\n"
        f"Phone: {book.Phone}\n\n"
        f"Location: {book.Location}\n\n"
        f"Service: {book.Service}\n\n"
        f"Details:{book.message}\n\n"
    )
    message = client.messages.create(
        body= message_body, 
        from_='whatsapp:+14155238886',
        to='whatsapp:+918015153921'
    )

def view_booking(request):
     return render(request,"view_booking.html")

 

def get_details(requst):
    books=list(Plumber.objects.values())
    return JsonResponse(books,safe=False)
