from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d={'name':'Ashu','age':2}
    return render(request,'h1.html',context=d)

def jinja_operation(request):
    d={'a':100,'b':800,'c':890,'name':'Ashu'}
    return render(request,'h2.html',d)
