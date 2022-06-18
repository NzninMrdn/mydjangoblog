from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse("hello im about!")
    return render(request,'about.html')
def home(request):
    # return HttpResponse("hello im home!")
    return render(request,'home.html')