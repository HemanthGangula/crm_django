from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_protect
from .models import Record

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')

    return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return redirect('home')


def customer_records(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Login required to view this page.')
        return redirect('home')

    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        messages.error(request, 'Record not found.')
        return redirect('home')

    if request.method == 'POST':
        record.first_name = request.POST.get('first_name')
        record.last_name = request.POST.get('last_name')
        record.email = request.POST.get('email')
        record.phone = request.POST.get('phone')
        record.address = request.POST.get('address')
        record.city = request.POST.get('city')
        record.state = request.POST.get('state')
        record.zipcode = request.POST.get('zipcode')
        record.save()
        messages.success(request, 'Record updated successfully!')
        return redirect('home')

    return render(request, 'customer_records.html', {'record': record}) 