from django.shortcuts import render, redirect
from django.contrib import messages
from website .models import Record

def customer_list(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Login required to view customer records.')
        return redirect('login')
    else:
        records = Record.objects.all()
        return render(request, 'customer_list.html', {'records': records})

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

def add_record(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Login required to add a record.')
        return redirect('home')

    if request.method == 'POST':
        record = Record(
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            address=request.POST.get('address', ''),
            city=request.POST.get('city', ''),
            state=request.POST.get('state', ''),
            zipcode=request.POST.get('zipcode', '')
        )
        record.save()
        messages.success(request, 'Record added successfully!')
        return redirect('home')

def update_record(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Login required to update a record.')
        return redirect('home')

    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        messages.error(request, 'Record not found.')
        return redirect('home')

    if request.method == 'POST':
        record.first_name = request.POST.get('first_name', record.first_name)
        record.last_name = request.POST.get('last_name', record.last_name)
        record.email = request.POST.get('email', record.email)
        record.phone = request.POST.get('phone', record.phone)
        record.address = request.POST.get('address', record.address)
        record.city = request.POST.get('city', record.city)
        record.state = request.POST.get('state', record.state)
        record.zipcode = request.POST.get('zipcode', record.zipcode)
        record.save()
        messages.success(request, 'Record updated successfully!')
        return redirect(f'/customer/{pk}')

    return render(request, 'update_record.html', {'record': record})

def delete_customer(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, 'Login required to delete a record.')
        return redirect('home')

    try:
        record = Record.objects.get(pk=pk)
        record.delete()
        messages.success(request, 'Record deleted successfully!')
    except Record.DoesNotExist:
        messages.error(request, 'Record not found.')

    return redirect('home')
