from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, Addrecordform
from .models import CRM
# Create your views here.

def home(request):
    records = CRM.objects.all()
    context = {}
    #logic to see logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials , try again or register first")
            return redirect('/')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "you have been logged out")
    return redirect('/')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def see_record(request, pk):
    if request.user.is_authenticated:
        customer_record = CRM.objects.get(id=pk)
        return render(request,'record.html',{'record': customer_record})

def delete_record(request, pk):
    if request.user.is_authenticated:

        del_record = CRM.objects.get(id=pk)
        del_record.delete()


        messages.success(request, "record deleted successfully")
        return redirect('home')




def update_record(request, pk):
    if request.user.is_authenticated:
        old_record = CRM.objects.get(id=pk)
        form = Addrecordform(request.POST or None, instance=old_record)
        if form.is_valid():
            form.save()
            messages.success(request, "record updated successfully")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "Please login first")
        return redirect('home')

def add_record(request):
    form = Addrecordform(request.POST or None)
    if request.user.is_authenticated:

        if request.method == 'POST':
            if form.is_valid():
                addedrec = form.save()
                messages.success(request, "record added successfully")
                records = CRM.objects.all()
                return render(request, 'home.html', {'records': records})

        return render(request, 'add_record.html', {'form':form})

    else:
        messages.error(request, "you must be logged in ")
        return redirect('home')


