from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Profile2



from myApp import models
from .models import Member
from .models import profile

from .models import Complaints



# Create your views here.
def logoutpage(request):
    logout(request)
    
    return redirect('homepage')



def basicwebsite(request):

    return render (request,'Basicwebsites.html')

def Homepage(request):
    return render (request,'HOMEPAGE.html')

def Sushimenu(request):
    return render (request,'sushifood.html')

def aboutus(request):
    return render (request, 'AboutUs.html')

def Menu(request):
    return render(request,'Menu.html')

def userprofile(request):
    return render(request,'userprofile.html')

def addmobile(request):
    return render(request,'addmobile.html')

def enterotp(request):
    return render(request,'enterotp.html')

def CustomerOrderList(request):
    return render (request,'CustomerOrderLists.html')

def Contact(request):
    
    if request.method =='POST':
        name = request.POST.get('sendername')
        email = request.POST.get('senderemail')
        phone = request.POST.get('senderphone')
        company = request.POST.get('sendercompany')
        message = request.POST.get('sendermessage')

        ins = models.Complaints(Name = name, Email = email, Phone = phone,CompanyName = company,Message = message)
        messages.success(request,'We have recieved your message, we will contact you soon!!!')
        ins.save()



    return render (request,'Contacts.html')

def foodloginform(request):
   
    if request.method=='POST':
        uname = request.POST.get('Username1')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        contact = request.POST.get('number')
        username = request.POST.get('Username2')
        pass3 = request.POST.get('pass')
       

    

        try:
            user = User.objects.filter(username= uname)

            if user.exists():
                return HttpResponse("Username already exit...")
       
            if pass1!=pass2:
                return HttpResponse("both passwords are does not match...")
        
        
            else:
                my_user = User.objects.create_user(uname,email,pass2)
                my_user.save()
                ins = models.Member(username = uname,email = email,contact = contact)
                ins.save()
                return redirect('loginform')
        
        except:
            user = authenticate(request,username=username,password=pass3)
            if user is not None:
                login(request,user)
            

                return redirect('homepage')
        
            else:
                return HttpResponse("Username or password is incorrect!!!")
            
       

       


    return render(request,'Loginform.html')




def Burgermenu(request):
    return render (request,'Burger.html')

def Pizzamenu(request):
    return render (request,'Pizzafood.html')

def Sandwichmenu(request):
    return render(request,'Sandwiches.html')

@login_required(login_url="/login/")
def paymentform(request):
    return render (request,'paymentform.html')
        


def registerpage(request):
    
    return render (request,'Registerpage.html')


def loginpage(request):
   
    return render (request,'loginpage.html')

def changeuserpass(request):
    if request.method=='POST':
        username = request.POST.get('Username3')
        newpass = request.POST.get('newpass')
        user = User.objects.get(username=username)
        user.set_password(newpass)
        user.save()


    
        return redirect('loginpage')

    return render (request,'changeuserpass.html')



def removeuser(request):
    if request.method=='POST':
        username = request.POST.get('Username4')
        pass23 = request.POST.get('pass23')
        user = authenticate(request,username=username,password=pass23)
        user.delete()
        return redirect('loginpage')
        
        

    return render (request,'deleteuser.html')


def uploadfile(request):
    if request.method=='POST':
        fullname = request.POST.get('Fullname')
        email = request.POST.get('fileemail')
        mobile = request.POST.get('filenumber')
        file = request.POST.get('fileupload')

        ins = models.profile(name = fullname,email = email,contact = mobile,image_field = file)
        ins.save()


    return render (request,'fileupload.html')



def profilepage(request):
    return render (request,'profile.html')

def practicepage(request):
    all_members = Member.objects.all
    return render (request,'practice.html',{'all': all_members})

def complaintstable(request):
    all_members = Complaints.objects.all
    return render (request,'complaintstable.html',{'all':all_members})


def form(request):
    return render (request,'form.html')

def Resetpassword(request):
    return render (request,'Resetpass.html')










        
      
