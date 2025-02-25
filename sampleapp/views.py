from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import contact_for
# from django.http import HttpResponse
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def index(request):
    return render(request,'index.html')

#validation register
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from django.contrib.auth.models import User

def log_reg(request):
    context={}
    if request.method == "POST":
        if request.POST.get('form_type')=='login_form': 
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
            #validate register
        elif request.POST.get('form_type')=='register_form':
             
    
               username = request.POST.get('username')
               email = request.POST.get('email')
               password = request.POST.get('password')
        
        # Check if username already exists
               if User.objects.filter(username=username).exists():
                  messages.error(request, 'Username already exists')
                  context['form_type'] = 'register_form'
                  return render(request, "log_reg.html", {"form_type": "register_form"})  # Example

               else:
            # Create new user and save to database
                  user = User.objects.create_user(username=username, email=email, password=password)
                  user.save()
                  messages.success(request, 'Account successfully created')
                  return redirect('log_reg')
        
        # return redirect("log_reg")  # Redirect to the login page after successful registration
    
    return render(request, 'log_reg.html')  # Render the registration page

#logout validation
def logout_view(request):
    logout(request)
    messages.success(request,'successfully logout')  
    return redirect("log_reg")
# contact validation
# def contact(request):
#     if request.method=="POST":
#         if request.POST.get('form_type')=='contact_form':
#             firstname=request.POST.get('first_name')
#             email=request.POST.get('email')
#             subject=request.POST.get('subject')
#             message=request.POST.get('message')
#             if not firstname or not email or not subject or not message:
#                 messages.error(request,'please fill all the fields') 
#             else:
#                 Ind=contact_for.objects.create(first_name=firstname,email=email,subject=subject,message=message)
#                 Ind.save()
#                 messages.success(request,"Message have been send,Thank you!")
#                 return redirect('contact')

        # return render(request,'contact.html')
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import contact_for  # Ensure the model is imported correctly

def contact(request):
    if request.method == "POST":
        if request.POST.get('form_type') == 'contact_form':
            firstname = request.POST.get('first_name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            # Check if any field is empty
            if not firstname or not email or not subject or not message:
                messages.error(request, 'Please fill all the fields')
            else:
                try:
                    # Create and save the contact entry
                    contact_entry = contact_for.objects.create(
                        first_name=firstname, 
                        email=email, 
                        subject=subject, 
                        message=message
                    )
                    # Optionally, save it again (redundant as .create() already saves)
                    # contact_entry.save()  
                    messages.success(request, "Message has been sent. Thank you!")
                    return redirect('contact')  # Ensure 'contact' URL is correct

                except Exception as e:
                    # Handle any errors
                    messages.error(request, f"An error occurred: {e}")

    return render(request, 'contact.html')

# Create your views here.