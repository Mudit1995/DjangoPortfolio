from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def signup(request):
    print('form submitted')
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('password1')
        get_confirm_password = request.POST.get('password2')

        print(get_email,get_confirm_password,get_password)

        if get_password != get_confirm_password:
            print('Passwords do not match')
            messages.info(request, 'Passwords do not match')
            return redirect('/AuthApp/signup')  # Use named URL instead of hardcoding

        # Check if email is already taken
        try:
            if User.objects.get(username=get_email):
                print('Email already taken')
                messages.warning(request, 'Email already taken')
                return redirect('/AuthApp/signup')
        except Exception as Identifier:
            pass  # Email is available

        # Create new user
        user = User.objects.create_user(username=get_email, email=get_email, password=get_password)
        user.save()

        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('/AuthApp/login')  # Redirect to login after successful signup

    return render(request, 'signup.html')

def hanlogin(request):
    if request.method == "POST":
        print('form submitted')
        get_email = request.POST.get('email')
        get_password = request.POST.get('password1')  # Use the correct field name
        
        # Authenticate the user
        myuser = authenticate(username=get_email, password=get_password)
        
        if myuser is not None:
            login(request, myuser)  # Use 'auth_login' to avoid conflict with the view name
            messages.success(request, 'Login successful!')
            return redirect('/')  # Redirect to home or another page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/AuthApp/login/')  # Stay on login page if credentials are invalid

    return render(request, 'login.html')
def hanlogout(requests):
    logout(requests)
    messages.success(requests, 'Logout successful!')
    return render(requests,'login.html')




