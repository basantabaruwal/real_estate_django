from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


def register(request):
    if request.method == "POST":
        # return register form
        # return HttpResponse("Registered")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']


        # check if the passwords match
        if password == password2:
            # check for duplicate username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "Opps! Username '{}' is already taken.".format(username))
                # return with same data
                data = {
                    'values': request.POST
                }
                return render(request, 'auth/register.html', data)
            else:
                # check for duplicate email
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, "Opps! Email '{}' is already taken.".format(email))
                # return with same data
                    data = {
                        'values': request.POST
                    }
                    return render(request, 'auth/register.html', data)
                else:
                    # Everything looks good
                    # register/create the user
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # redirect the user to login page with a good success info
                    messages.success(request, "Registration successful. Please login to proceed.")
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            # return with same data
            data = {
                'values': request.POST
            }
            return render(request, 'auth/register.html', data)

        return render(request, 'auth/register.html')
    else:
        # implement logging in logic
        return render(request, 'auth/register.html')


def login(request):
    if request.method == "POST":
        # implement logging in logic
        username = request.POST['username']
        password = request.POST['password']

        # attempt to login
        user = auth.authenticate(username=username, password=password)
        if user is not None: # user exists
            auth.login(request, user)
            messages.success(request, "You're now Logged In")
            return redirect('dashboard')
        else: # user doesn't exist
            messages.error(request, "Invalid Credentials!")
            return redirect('login')

    else:
        # return login form
        data = {
            'page_title': 'Login'
        }
        return render(request, 'auth/login.html', data)


def logout(request):
    if request.method == 'POST':
        # Implement Logout logic
        auth.logout(request)
        # if logout successfull, redirect to home
        messages.info(request, "You're logged out.")
        return redirect('home')

    return HttpResponse('Logged Out')


def dashboard(request):
    return render(request, 'auth/dashboard.html')
