from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import AeducationalForm, RegistrationForm
from .models import AoneEducational, Account

# Create your views here.


def home(response):
    return render(response, "aoneedu/home.html", {})

def rules_v(response):
    return render(response, "aoneedu/rules.html", {})

def aboutus_v(response):
    return render(response, "aoneedu/members.html", {})


def coursespage(response):
    user = response.user

    if user.is_authenticated:
        form = AeducationalForm()
        
    else:
        messages.warning(response, "Your account is about to expire.") 
        return redirect("/login")
    
    return render(response, "aoneedu/courses.html", {})



def examsform(request):
    user = request.user

    if user.is_authenticated:

        if request.method == "POST":
            form = AeducationalForm(request.POST)
            if form.is_valid():

                examform = form.save(commit=False)
                examform.owner = request.user
                examform.save()

                return redirect("/viewedit")
            
        else:

                
            form = AeducationalForm()
    else:
        return redirect("/login")
    return render(request, "aoneedu/utme.html", {"form":form})



def updateforms(request, aoneEducational_id):
    user = request.user

    if user.is_authenticated:

        uforms  =   AoneEducational.objects.get(pk=aoneEducational_id)
        form = AeducationalForm(request.POST or None, instance=uforms)
        if form.is_valid():
            form.save()
            return redirect("/viewedit")
    else:
        return redirect("/login")
    return render(request, "aoneedu/updateform.html", {"uforms":uforms, "form":form})


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"User is already authenticated as {user.email}.")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("/")
        else:
            context["registration_form"] = form

    return render(request, "aoneedu/register.html", context)


def loguserout(request):
    logout(request)
    return redirect("/login")



def formviews(response, aoneEducational_id):
    user = response.user

    if user.is_authenticated:
        ls  =   AoneEducational.objects.get(pk=aoneEducational_id)

    else:
        return redirect("/login")
    return render(response, "aoneedu/lis.html", {"ls":ls})





def viewedit(response):

    user = response.user

    if user.is_authenticated:
        
        lists  =   AoneEducational.objects.all()

    else:
        return redirect("/login")
    return render(response, "aoneedu/waecneco.html", {"lists":lists})

