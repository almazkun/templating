from django.shortcuts import render

# Create your views here.
def x(request):
    return render(request, 'x.html')

def y(request):
    return render(request, 'y.html')

def omg(request):
    return render(request, 'omicron.html')