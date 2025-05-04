from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'selamat_datang.html')

def tentang(request):
    
    return render(request,'tentang.html')