from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from user.models import CustomUser
from .forms import LoginForm, RegisterForm, NewUserForm
from django.contrib.auth import authenticate, login, logout


def log_in(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                context = {'form': form}
                messages.error(request, "Login failed. Check your credentials")
                return render(request, 'authentication/login.html', context)
        else:
            context = {'form': form}
            return render(request, 'authentication/login.html', context)


    # Jeżeli GET to przesłanie pustego formularza
    else:
        context = {'form': LoginForm()}
        return render(request, 'authentication/login.html', context)
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = NewUserForm(request.POST)
        try:
            user = User.objects.get(username=request.POST['username'])
            if user is not None:
                messages.warning(request, "User with username: " + request.POST['username'] + " exists. Choose another username")
                return redirect("register")

        except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                customUser=CustomUser.objects.create(user=user,first_name="",last_name="",phone="",street="",city="",state="",zip_code="",image="\images\defaultImage.png")
                # user = form.save()
                login(request, user)
                messages.success(request, "Registration successful")
                return redirect("home")

    form = NewUserForm()
    return render (request=request, template_name="authentication/register.html", context={"register_form":form})

