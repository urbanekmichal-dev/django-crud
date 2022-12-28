from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, NewUserForm
from django.contrib.auth import authenticate, login, logout


def log_in(request):
    # Sprawdzenie czy użytkownik jest zalogowany
    # Jeżeli tak - przekierowanie go na stronę z listą wiadomości
    if request.user.is_authenticated:
        return redirect('home')

    # Sprawdzenie jakiego typu jest zapytanie HTTP
    # Jeżeli POST - próba zalogowania użytkownika
    if request.method == 'POST':

        # Wykorzytanie formularza do sprawdzenia czy wszystkie dane zostały wpisane
        form = LoginForm(request.POST)
        if form.is_valid():

            # Wykorzytanie wbudowanego systemu autentykacji w Django
            # do sprawdzenia czy użytkownik istnieje w bazie danych
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            # Jeżeli uzytkownik istnieje - zalogowanie go
            # i przekierowanie na stronę z wiadomościami
            if user is not None:
                login(request, user)
                return redirect('home')


            # Jeżeli nie istnieje lub przesłane dane są niepełne - przesłanie
            # klientowi z powrotem formularza z danymi
            else:
                context = {'form': form}
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

# def register(request):
#     if request.user.is_authenticated:
#         return redirect('view_news')
#
#     if request.method == 'POST':
#
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             context = {'form': form}
#             return render(request, 'authentication/register.html', context)
#         else:
#             context = {'form': RegisterForm()}
#             return render(request, 'authentication/register.html', context)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="authentication/register.html", context={"register_form":form})