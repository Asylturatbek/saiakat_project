from django.shortcuts import render

def register(request):
    if request.method=='GET':
        return render(request,'register.html')
    elif request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
