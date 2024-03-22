from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import CRM
# Create your views here.
records = CRM.objects.all()
def home(request):

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

        recordie = CRM.objects.all()
        messages.success(request, "record deleted successfully")
        return render(request,'home.html',{'records': recordie})



