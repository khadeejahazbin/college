from django.contrib.auth.models import User
from django.contrib import auth, messages

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


from .models import Department


# Create your views here.
def allDepart(request, d_slug=None):
    d_page = None
    departments = None
    if d_slug != None:
        d_page = get_object_or_404(Department, slug=d_slug)
    return render(request, "department.html", {'department': d_page})




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return render(request,'register.html')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return render(request, 'login.html')
        else:
            messages.info(request, 'password not matching')
            return render(request, "register.html")

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'newpage.html')
        else:
            messages.info(request,'invalid user')
            return render(request,'login.html')
    return render(request,'login.html')

def newpage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        DOB = request.POST['DOB']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        course = request.POST['course']
        purpose = request.POST['purpose']
        material_provide = request.POST['material_provide']
        user = User.objects.create_user(email=email, first_name=first_name)
        user.save();
        return render(request, 'linkpage.html')
    return render(request,'newpage.html')
#
def linkpage(request):
    if request.method == 'POST':
      return redirect('/')
    return render(request, 'linkpage.html')

def logout(request):
    auth.logout(request)
    return redirect('/')