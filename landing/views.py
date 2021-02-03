from django.shortcuts import render,get_object_or_404
from .models import Event,Registration
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.utils.crypto import get_random_string


def home(request):
    queryset = Event.objects.filter()[:6]
    for e in queryset:
        print(e.course_id.course_logo.url)
    # fetch_event = get_object_or_404(queryset,slug=slug)
    return render(request, "main/index.html",{'queryset':queryset})

def eventpage(request,slug):
    eventfetch = get_object_or_404(Event,event_slug=slug)
    return render(request,"main/eventpage.html",{"eventfetch":eventfetch})


def contactform1(request):
    if request.method == 'POST':
        name_captured = request.POST['name']
        email_captured = request.POST['email']
        subject_captured = request.POST['subject']
        message_captured = request.POST['message']
        admin_mail = "contact-us@accelerators.co.uk"
        subject = "New Message @ accelerators from : " + name_captured
        message = "Sender: " + name_captured + ",   sender email: " +   email_captured + " ,  Message: " + message_captured
        try:
            send_mail(subject, message, admin_mail,['anuragsingh1987@gmail.com','Preethi.Gunasekara@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('Email sent. We will contact you shortly')
    return HttpResponse('Something Went wrong !!')

def contactform2(request):
    if request.method == 'POST':
        email_captured = request.POST['email']
        admin_mail = "contact-us@accelerators.co.uk"
        subject = "New Subscription Request @ CIO Site from :  " + email_captured
        message = "Please add  " + email_captured + " to accelerators Newletters "
        try:
            send_mail(subject, message, admin_mail,['anuragsingh1987@gmail.com','Preethi.Gunasekara@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponse('We have added you the Accelerators DL.')
    return HttpResponse('Something Went wrong !!')


# def RegisterForm(request,slug):
#     if request.method == 'POST':
#         name_captured = request.POST['name']
#         email_captured = request.POST['email']
#         subject_captured = request.POST['subject']
#         message_captured = request.POST['message']
#         admin_mail = "contact-us@accelerators.co.uk"
#         subject = "New Message @ accelerators from : " + name_captured
#         message = "Sender: " + name_captured + ",   sender email: " +   email_captured + " ,  Message: " + message_captured
#         try:
#             eventfetch = get_object_or_404(Event,event_slug=slug)
#             print(slug)
#             first_bit = name_captured[0:3]
#             unique_id = get_random_string(length=6,allowed_chars='AZXY123BFG')
#             registration_unique_id = name_captured[0:3] + unique_id
#             print(registration_unique_id)
#             send_mail(subject, message, admin_mail,['anuragsingh1987@gmail.com','Preethi.Gunasekara@gmail.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponse('We have sent you an email with the Payment Details. Please process the payment secure a spot in the event')
#     return HttpResponse('Something Went wrong !!')
#

def RegConfirm(request):
    if request.method == 'POST':
        fname_captured = request.POST['fname']
        lname_captured = request.POST['lname']
        email_captured = request.POST['email']
        contact_captured = request.POST['contact']
        coupon_captured = request.POST['coupon']

        try:
            first_bit = fname_captured[0:3]
            unique_id = get_random_string(length=6,allowed_chars='AZXY123BFG')
            registration_unique_id = fname_captured[0:3] + unique_id
            print(registration_unique_id)
            slug="Scaled-Agile-London"
            eventfetch = get_object_or_404(Event,event_slug=slug)
            x = Registration(event_id=eventfetch,registration_fname=fname_captured,registration_lname=lname_captured,registration_email=email_captured,registration_contact_number=contact_captured,registration_unique_id=registration_unique_id,registration_coupon_code=coupon_captured,registration_paid_status="False")
            x.save()
            admin_mail = "contact-us@accelerators.co.uk"
            message = "thanks for registering "
            subject = "New Registration @ accelerators - Unique Code  :" + registration_unique_id
            send_mail(subject, message, admin_mail,['anuragsingh1987@gmail.com','Preethi.Gunasekara@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request,'main/registrationdone.html')

    return HttpResponse('Something Went wrong !!')
