from django.shortcuts import render
#from django.http import HttpResponse 
# Create your views here.

def usermodel(request):
    x={'name':'ahmed', 'age':25}
    return render(request, 'pages/index.html', x)
    #return HttpResponse('Hello')

def bookmodel(request):
    return render(request, 'pages/bookmodel.html')