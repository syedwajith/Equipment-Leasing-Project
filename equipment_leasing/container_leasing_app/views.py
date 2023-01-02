from django.shortcuts import render,HttpResponse,redirect
from container_leasing_app.models import LessorDetails,LesseeDetails,ContainerDetails,LeasingDetails

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

def adminlogout(request):
    return redirect('/container_leasing_app/containerhome')

def admin_lessorpending(request):
    return render(request, 'container_leasing_app/lessorpending.html')

def admin_lessorapprove(request):
    return render(request, 'container_leasing_app/lessorapprove.html')

def admin_lesseepending(request):
    return render(request, 'container_leasing_app/lesseepending.html')

def admin_lesseeapprove(request):
    return render(request, 'container_leasing_app/lesseeapprove.html')

# Lessor
def lessorlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            LessorDetails.objects.get(Username=username, Password=password)
            return redirect('/container_leasing_app/lessor_home')
        except:
            return HttpResponse('Invalid Username and Password')
    return render(request, 'container_leasing_app/lessorlogin.html')

def home_lessor(request):
    return redirect('/container_leasing_app/lessorlogin')

def lessor_register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        lessor = LessorDetails()
        if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(phoneno) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            return HttpResponse('Please fill the all fields')
        elif password != confirmpassword:
            return HttpResponse('password is mismatch')
        else:
            lessor.First_Name = firstname
            lessor.Last_Name = lastname
            lessor.Email = email
            lessor.Phone_No = phoneno
            lessor.Country = country
            lessor.State = state
            lessor.City = city
            lessor.Username = username
            lessor.Password = password
            lessor.save()
            return redirect('/container_leasing_app/lessorlog')
    return render(request, 'container_leasing_app/lessorregister.html')

def lessor_log_reg(request):
    return redirect('/container_leasing_app/lessor_register')

def lessor_home(request):
    return render(request, 'container_leasing_app/lessorhome.html')

def lessorlogout(request):
    return redirect('/container_leasing_app/containerhome')

def lessor_editprofile(request):
    return render(request, 'container_leasing_app/lessor_editprofile.html')

def lessor_addcontainer(request):
    return render(request, 'container_leasing_app/lessor_addcontainer.html')

def lessor_updatecontainer(request):
    return render(request, 'container_leasing_app/lessor_updatecontainer.html')

def lessor_view_leased_container(request):
    return render(request, 'container_leasing_app/lessor_viewleasedcontainer.html')

# Lessee
def lesseelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            LesseeDetails.objects.get(Username=username, Password=password)
            return redirect('/container_leasing_app/lessee_home')
        except:
            return HttpResponse('Invalid Username and Password')
    return render(request, 'container_leasing_app/lesseelogin.html')
    
def home_lessee(request):
    return redirect('/container_leasing_app/lesseelogin')

def lessee_register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        company = request.POST.get('company')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        lessee = LesseeDetails()
        if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(phoneno) == 0 or len(company) == 0 or len(country) == 0 or len(state) == 0 or len(city) == 0 or len(username) == 0 or len(password) == 0 or len(confirmpassword) == 0:
            return HttpResponse('Please fill the all fields')
        elif password != confirmpassword:
            return HttpResponse('password is mismatch')
        else:
            lessee.First_Name = firstname
            lessee.Last_Name = lastname
            lessee.Email = email
            lessee.Phone_No = phoneno
            lessee.Company = company
            lessee.Country = country
            lessee.State = state
            lessee.City = city
            lessee.Username = username
            lessee.Password = password
            lessee.save()
            return redirect('/container_leasing_app/lesseelog')
    return render(request, 'container_leasing_app/lesseeregister.html')

def lessee_log_reg(request):
    return redirect('/container_leasing_app/lessee_register')

def lessee_home(request):
    return render(request, 'container_leasing_app/lesseehome.html')
    
def lesseelogout(request):
    return redirect('/container_leasing_app/containerhome')

def lessee_editprofile(request):
    return render(request, 'container_leasing_app/lessee_editprofile.html')

def lessee_view_container_list(request):
    return render(request, 'container_leasing_app/lessee_viewcontainerlist.html')

def lessee_view_leasing_list(request):
    return render(request, 'container_leasing_app/lessee_viewleasinglist.html')

