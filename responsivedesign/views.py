from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'design/home.html', context)

def productsresponsive(request):
    context = {}
    return render(request, 'design/productsresponsive.html', context)

def peopleresponsive(request):
    context = {}
    return render(request, 'design/peopleresponsive.html', context)
    
def contactus(request):
    context = {}
    return render(request, 'design/contactus.html', context)
