from django.shortcuts import render

# Create your views here.
def specific1(request):
    return render(request,'specific1.html')

def specific2(request):
    return render(request,'specific2.html')