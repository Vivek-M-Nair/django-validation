from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
# from django.http import HttpResponse
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def index(request):
    return render(request,'index.html')
# def log_reg(request):
#     return render(request,'log_reg.html')

#validation register
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('log_view')
        else:
            # Create new user and save to database
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account successfully created')
            return redirect('log_view')
        
        # return redirect("log_reg")  # Redirect to the login page after successful registration
    
    return render(request, 'log_reg.html')  # Render the registration page

def log_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('contact')  # Redirect to the contact page after successful login
        else:
            messages.error(request, 'Incorrect username or password')  # Show error message if authentication fails
            # return render(request, 'log_reg.html')  # Render the login page
    
    return render(request, 'log_reg.html')  # Render the login page for GET request

#logout validation
def logout_view(request):
    logout(request)
    messages.success(request,'successfully logout')  
    return redirect("log_reg")

# Create your views here.