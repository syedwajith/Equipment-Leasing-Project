from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def ContainerHome(request):
    return render(request, 'container_leasing_app/containerhome.html')

def adminlogin(request):
    return render(request, 'container_leasing_app/adminlogin.html')

def home_admin(request):
    return redirect('/container_leasing_app/adminlogin')

def lessorlogin(request):
    return render(request, '/container_leasing_app/lessorlogin.html')

def home_lessor(request):
    return redirect('/container_leasing_app/lessorlogin')

def lesseelogin(request):
    return render(request, '/container_leasing_app/lesseelogin.html')
    
def home_lessee(request):
    return redirect('/container_leasing_app/lesseelogin')