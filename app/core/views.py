from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")
def health(request):
    return render(request, "core/health.html")
def farming(request):
    return render(request, "core/farming.html")
def education(request):
    return render(request, "core/education.html")
def emergency(request):
    return render(request, "core/emergency.html")
