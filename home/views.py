from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# username for testuser ankitsingh
# password for testuser is Ankit123
def index(request):
    print(request.user)
    if request.user.is_anonymous:
      return redirect("/login")
    # return HttpResponse("My name is ankit")
    return render(request,'index.html')
def loginUser(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        # check if user has entered correct crediantials
        user = authenticate(username=username,password=password)
        
        if user is not None:
         login(request,user)
         return  redirect("/")
    #  index.html 
            # a backend will authenticate the crediantials
        
        else:
         # no backend authenticate the crediantials
              return render(request,'login.html')
    return render(request,'login.html')
    #  login.html
        
    # return HttpResponse("My name is ankit singh")
        # return render(request,'login.html')
def logoutUser(request):
    logout(request)
    # return HttpResponse("My name is ankit")
    # return render(request,'login.html')
    return redirect("/login")
# Create your views here.
