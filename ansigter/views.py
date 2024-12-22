from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})

def modules_view(request):
    return render(request, "modules.html", {})

def training_view(request):
    return render(request, "training.html", {})