from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

# Main page
def ContainerHome(request):
    return render(request, 'container_leasing_app/containerhome.html')

# Admin
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
            return redirect('/container_leasing_app/adminhome')
        else:
            return HttpResponse('Invalid')
    return render(request, 'container_leasing_app/adminlogin.html')

def adminhome(request):
    return render(request, 'container_leasing_app/adminhome.html')

def home_admin(request):
    return redirect('/container_leasing_app/adminlogin')

# Lessor
def lessorlogin(request):
    return render(request, 'container_leasing_app/lessorlogin.html')

def home_lessor(request):
    return redirect('/container_leasing_app/lessorlogin')

def lessor_register(request):
    return render(request, 'container_leasing_app/lessorregister.html')

def lessor_log_reg(request):
    return redirect('/container_leasing_app/lessor_register')

# Lessee
def lesseelogin(request):
    return render(request, 'container_leasing_app/lesseelogin.html')
    
def home_lessee(request):
    return redirect('/container_leasing_app/lesseelogin')

def lessee_register(request):
    return render(request, 'container_leasing_app/lesseeregister.html')

def lessee_log_reg(request):
    return redirect('/container_leasing_app/lessee_register')
