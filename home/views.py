from django.shortcuts import render,redirect
from django.http import HttpResponse, request
# now for using login sys we import user model
from django.contrib.auth.models import User,auth
from django.contrib.auth  import authenticate,  login, logout


# Create your views here.
def home(request):
    print(User.is_authenticated)
    if request.user.is_authenticated:
        pass
    else:
        return redirect('/login')
    return render(request, 'homepage.html')

def paint(request):
    if request.method == 'GET':
        print('get')
    else:
        print('post')
        height = request.POST['height']
        width = request.POST['width']
        print(height,width)
        params={}
        params['height'] = height
        params['width'] = width
        print(params)
        return render(request,"canvas.html",params)
    return render(request, 'user_input.html')


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['cpassword']

        exist = User.objects.all().filter(email=email)
        print(exist)
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        # messages.success(request, " Your iCoder has been successfully created")
        print(" Your Account has been successfully created")
        return redirect('/login')
                  

    else:
        return HttpResponse("404 - Not found")



def loginpage(request):
    return render(request,'login.html')

def Handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        exist = User.objects.all().filter(username=username)
        print(exist)
        if len(exist)==0:
            print(" username not Found Please Sign Up")
            return redirect('/login')
        user=authenticate(username=username, password=password) 
        if user is not None:
            login(request, user)
            print("Successfully Logged In")
            print('loged in')
            return redirect("/")
        else:
            print("Invalid credentials! Please try again")
            return redirect("/login")
    else:
        return redirect('loginpage')

def logout(request):
    auth.logout(request)
    return redirect('/login')