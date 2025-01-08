from django.shortcuts import render


def home_view(request):
    return render(request, "home.html", {})

def modules_view(request):
    return render(request, "modules.html", {})

def training_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, "training.html", {})