# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from django.shortcuts import render, get_object_or_404, redirect
#
# from schools.models import Department
#
#
# # # Create your views here.
# # def allDepart(request, d_slug=None):
# #     d_page = None
# #     departments = None
# #     if d_slug != None:
# #         d_page = get_object_or_404(Department, slug=d_slug)
# #     return render(request, "department.html", {'department': d_page})
#
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         # if user is not None:
#         #     auth.login(request, user)
#         #     return redirect('/')
#
#         return render(request, 'newpage.html')
#     return render(request, 'login.html')
#
#
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'username taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save();
#         else:
#             messages.info(request, 'password not matched')
#             return redirect('register')
#
#         return render(request,'login')
#     return render(request, "register.html"),
#
#
# def newpage(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         DOB = request.POST['DOB']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone_no = request.POST['phone_no']
#         email = request.POST['email']
#         address = request.POST['address']
#         department = request.POST['department']
#         course = request.POST['course']
#         purpose = request.POST['purpose']
#         material_provide = request.POST['material_provide']
#         return render(request, 'linkpage.html')
#     return render(request, 'newpage.html')
#
#
# def linkpage(request):
#     if request.method == 'POST':
#         return redirect('/')
#     return render(request, 'linkpage.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')

# def login(request):
#     if request.method== 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         # if user is not None:
#         #     auth.login(request,user)
#         #     return redirect('/')
#         # else:
#         #     messages.info(request,'invalid credentials')
#         #     return redirect('login')
#     return render(request,'login.html')
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['password1']
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username taken')
#                 return redirect('register')
#             else:
#
#                 user = User.objects.create_user(username=username, password=password)
#                 user.save();
#                 return redirect('login')
#         else:
#            messages.info(request,'password not matching')
#            return redirect('register')
#         # return redirect('/')
#
#     return render(request, "register.html")
