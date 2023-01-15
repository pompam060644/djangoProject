from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def test(request):
    return HttpResponse("H1>Hello World <dr> This My World Wide Web")

def firstwed (request) :
    return render(request,'firstweb.html')

def secondpage (request) :
    return render(request,'secondpage.html')

def thirdpage (request) :
    return render (request,'thirdpage.html')
