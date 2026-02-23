from django.shortcuts import render
from .models import Horario, Linha

def index(request):
    return render(request, 'telas/index.html')

def search(request):
    origin = request.GET.get('origin', '')
    destination = request.GET.get('destination', '')
    
    
    # Simple filtering for demonstration
    results = Horario.objects.filter(
        linha__origem__icontains=origin,
        linha__destino__icontains=destination
    )
    
    context = {
        'results': results,
        'origin': origin,
        'destination': destination,
        
    }
    print("origem",origin)
    print("Destino",destination)
    print("Resultado",results.count()) 
    return render(request, 'telas/search_results.html', context)

def login_view(request):
    return render(request, 'telas/login.html')

def signup_view(request):
    return render(request, 'telas/signup.html')

def routes(request):
    return render(request, 'telas/routes.html')

def offers(request):
    return render(request, 'telas/offers.html')

def manage_booking(request):
    return render(request, 'telas/manage_booking.html')
