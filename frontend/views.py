from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import HttpResponseRedirect
import datetime
from .emailsender import sendmail
from django.conf import settings



# Create your views here.
def IndexView(request):

    context={'year':datetime.datetime.now().year}
    return render(request,'frontend/index.html',context)



def ContactView(request):
    if request.method == 'POST':
        # try:
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        phone=request.POST['phone']
        recipient_list=[settings.EMAIL_HOST_USER,]
    

        name=request.POST['name']
        
        # send_mail(
        #     subject=subject,
        #     message=message,
        #     from_email=email,
        #     recipient_list=recipient_list,
        #     # fail_silently=False
        # )
        sendmail(recipient_list,message,message,subject,email=email,name=str(email).split('@')[0])
        # Message.objects.create(
        #     subject=subject,
        #     email=email,
        #     message=message,
        #     phone=phone,
        #     name=name
        # )
        # except:
        #     raise TimeoutError('timeout expired')
    