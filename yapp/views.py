from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'yhome.html')
def calculate(request):
    height = request.POST['height']
    weight = request.POST['weight']
    bmi = round((int(weight)/int(height)**2),2)
    if bmi <= 18.5:
        result = "You are underweight"
    elif 18.5 < bmi <= 24.9:
        result = "Your weight is normal"
    elif 25 < bmi <= 29.29:
        result = "You are overweight."
    else:
        result = "You are obese."
    return render(request,'bmi.html',{'result':result})
