from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Information
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    """This view will render the request to home page"""
    return render(request, 'base.html')


def create(request):
    if request.method=='POST':
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        title = request.POST['blog_title']
        blog = request.POST['blog']
        email = request.POST['email']
        ob = Information.objects.filter(email=email)
        if ob:
            messages.warning(request, "email already exists, please try again with different password")

            return HttpResponseRedirect(reverse('create'))
        else:
            fm = Information.objects.create(firstname=fname, lastname=lname,
                                            blog_title=title, email=email, blog=blog)
            fm.save()
    data = Information.objects.all()
    context = {
        "data_info": data,
    }
    return render(request, 'crud.html', context)


def edit(request, id):
    if request.method == 'POST':
        obj = Information.objects.get(id=id)
        print(obj)
        obj.firstname = request.POST['firstname']
        obj.lastname = request.POST['lastname']
        obj.title = request.POST['blog_title']
        obj.blog = request.POST['blog']
        obj.email = request.POST['email']
        obj.save()
        return HttpResponseRedirect(reverse('create'))
    data = Information.objects.get(id=id)
    context = {
        'form': data
    }
    return render(request, 'edit.html', context)


def delete(request, id):
    '''This view is to delete the selected information.'''
    Information.objects.filter(id=id).delete()
    return render(request, 'confirm_delete.html')


def login(request):
    '''This is to login into the self profile.'''
    if request.method == 'POST':
        uname = request.POST['username']
        pswd = request.POST['password']
        obj = User.objects.filter(username='uname', password='pswd')
        if obj:
            HttpResponse("You are login")
        else:
            HttpResponse("Wrong Credentials")

    return render(request, 'login.html')






