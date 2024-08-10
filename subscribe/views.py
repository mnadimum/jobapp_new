from django.shortcuts import render, redirect
from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.urls import reverse


# Create your views here.

def subscribe(request):
    email_error_empty= ""
    
    subscribe_form = SubscribeForm()
    
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("Valid Form")
            # print(subscribe_form.cleaned_data)
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # email = subscribe_form.cleaned_data['email']
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            return redirect(reverse('thank_you'))
            
        #first_name = request.POST['firstname']
        #last_name = request.POST['lastname']
        #email = request.POST['email']
        
        
        # if email == "":
        #     email_error_empty="No email entered"
        # print("POST request", email)
        # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
        # subscribe.save()    
        
    context = {"form": subscribe_form,"email_error_empty": email_error_empty}
    
    return render(request, "subscribe/subscribe.html", context)

def thank_you(request):
    
    context = {}
    
    return render(request, "subscribe/thank_you.html", context)


    
    
