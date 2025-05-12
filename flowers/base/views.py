from django.shortcuts import render,redirect,get_object_or_404
from.models import flower,customer
from base.form import contactform, Order,BookingForm
from django.http import HttpResponse
from django .contrib .auth.forms import  AuthenticationForm



def home(request):
    return render(request,'base/home.html')

def flowers(request):
    myflowers=flower.objects.all()
    return render(request,'base/flowers.html',{'myflowers':myflowers})

def login(request):
    if request.method =='post':
        form= AuthenticationForm(data=request.post)
        if form.is_valid():
            login(request.form.get_user())
            form.save()
        return redirect('flowers.html')  
    else:
        form=AuthenticationForm()
        return render(request,'base/login.html',{'form':form})
def flower_list(request):
    Flowers = flower.objects.all()
    return render(request, 'base/flowerlist.html',{'flowers': Flowers})
    
def flower_detail(request, id):
     flowers = get_object_or_404(flower,id=id)
     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
         return render(request, 'base/flowerdetail_partial.html', {'flower': flowers})
     return render(request, 'base/flowerdetail.html', {'flower': flowers})


    


def contact(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.customer = customer.objects.first()  # Replace with real customer
            contact_instance.save()
            return redirect('order')
    else:
        form = contactform()
    return render(request, 'base/contact.html', {'form': form})

def order(request):
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            order_instance = form.save(commit=False)
            order_instance.customer = customer.objects.first()  # Replace with real customer
            order_instance.save()
            return redirect('booking')
    else:
        form = Order()
    return render(request, 'base/order.html', {'form': form})

def booking(request):
    

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.order = order  # ✅ Link booking to selected order
            booking_instance.save()
            return redirect('success')  # replace with your actual success URL
    else:
        form = BookingForm()

    return render(request, 'base/booking.html', {'form': form, 'order': order})

def success(request):
   return render(request,'base/success.html')
    
