from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Clothing/index.html", {
        "links": links
    })
    
def add(request):
    return render(request, "Clothing/add.html", {
        "links": links
    })