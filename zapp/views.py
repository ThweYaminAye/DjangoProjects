from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'zhome.html')
def userinfo(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    return render(request,'userinfo.html', {'name': name,'email': email, 'address': password})
