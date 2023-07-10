from django.contrib.auth import logout
from django.shortcuts import render , redirect , HttpResponse
from .models import logins  

# Create your views here.

def index(request):
    return render(request,"index.html")


def logout_view(request):
    logout(request)
    return redirect('login')

def login(request):
        if request.method == 'POST':
            if 'signup' in request.POST:
                    obj = logins()
                    obj.name = request.POST.get('name')
                    obj.password = request.POST.get('password')
                    obj.email = request.POST.get('email')

                    obj.save()
                    print("Saved Successfully")
                    return redirect('login')
            elif 'login' in request.POST:
            # Handle login form submission
                x = request.POST.get('lemail')
                y = request.POST.get('lpassword')
                try:
                    z = logins.objects.get(email=x)
                    if y == z.password:
                        return redirect('index')
                    else:
                        return HttpResponse("Invalid Password")
                except logins.DoesNotExist:
                    return HttpResponse("User does not exist")
    

        return render(request, "login.html")

