from django.shortcuts import render

# Create your views here.
def generic1(request):
    return render(request,'generic1.html')

def generic2(request):
    return render(request,'generic2.html')
