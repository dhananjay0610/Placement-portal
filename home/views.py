from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
from datetime import datetime
from home.models import Contact,Recruitment,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    organisation=Recruitment.objects.all()
    context={'organisation':organisation}
    return render(request,'home.html',context)


def student(request):
    return render(request,'student.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        decr=request.POST.get('decr')
        contact=Contact(name=name,email=email,phone=phone,decr=decr,date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def recruitment(request):
    organisation=Recruitment.objects.all()
    context={'organisation':organisation}
    return render(request,'recruitment.html',context)

def blog(request,slug):
    bpost=Recruitment.objects.filter(slug=slug).first()
    # bpost.save()
    context={'bpost':bpost}
    return render(request,'blogs.html',context)

@login_required(login_url='/student/')
def handleApplication(request):
    if request.method == "POST":
        user=request.user
        postsno=request.POST.get('sno')
        post=Recruitment.objects.get(sno=postsno)
        post.user.add(user)
        post.save()
    return redirect('recruitment')

def handlesignup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if len(username) >12:
             messages.error(request,'User name must be under 12 characters')
             return redirect('student')
        if not username.islower():
             messages.error(request,'User name must be in lowercases')
             return redirect('student')
        if not username.isalnum()  :
             messages.error(request,'User name must contain letters and numbers')
             return redirect('student')
        if pass1 != pass2 :
             messages.error(request,'your password is not matched correctly')
             return redirect('student')

        myuser = User.objects.create_user(username,email,pass1)
        # myuser.save()
        fname=request.POST['fname']
        lname=request.POST['lname']
        roll=request.POST['roll']
        address=request.POST['address']
        branch=request.POST['branch']
        info=Profile(username=myuser,roll=roll,address=address,branch=branch,fname=fname,lname=lname)
        info.save()
        messages.success(request,'your account has been successfully created')
        return redirect('student')

    else:
        return HttpResponse('Not allowed')

def handlelogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        user = authenticate(username = loginusername,password = loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,'successfully loged-in')
            return redirect('studentInfo')
        else:
            messages.error(request,'invalid credentials')
            return redirect('student')

    return HttpResponse('Not allowed')

def handlelogout(request):
    logout(request)
    messages.success(request,"you had successfully loged-out")
    return redirect('student')

@login_required(login_url='/student/')
def studentInfo(request):
    name=Profile.objects.filter(username=request.user)
    recruitment=Recruitment.objects.filter(user=request.user)
    context={'name':name,'recruitment':recruitment}
    return render(request,'studentInfo.html',context)
