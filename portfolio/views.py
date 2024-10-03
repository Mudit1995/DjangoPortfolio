from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

from .models import *


def home(request):

    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')



def contact(request):
    
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phonenumber = request.POST['Phonr_number']
        description = request.POST['desc']
        print(name,email,phonenumber,description)
        query_contact = Contact(name=name, email=email, phonenumber=phonenumber, description=description)
        query_contact.save()
        messages.success(request, 'Your message has been sent successfully')
        messages.info(request,f'the name is {name}, the email is {email}, the phone number is {phonenumber} and your query is {description} have reached us')
        return redirect('/contact')


#  data us storied in the form of the objects in the 

    return render(request, 'contact.html')




def handleblogs(requests):
    posts = blogs.objects.all()
    for i in posts:
    #     print(i.description)
    #     print(i.authorname)
    #     print(i.title)
    #     print(i.date)
        print(i.image)
    context = {"posts":posts}
    print(context)
    return render(requests,"handleblog.html",context)


def resume(request):
    return render(request,"resume.html")