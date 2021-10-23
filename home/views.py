from django.shortcuts import render

# Create your views here.

def index(request):
    """ Veiw returns home page (index.html)"""
    
    return render(request, 'home/index.html')