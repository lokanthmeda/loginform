from django.shortcuts import render
from .models import register
from .forms import registered, login
from django.http.response import HttpResponse
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        rfor = registered(request.POST)
        if rfor.is_valid():
            username = request.POST.get('username')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')

            data = register(

                username=username,
                mobile=mobile,
                password=password,

            )
            data.save()

            return render(request, 'register.html', {'form': rfor})
    else:
        rfor = registered()
        context = {'form': rfor}
        return render(request, 'register.html', context)


def login_view(request):
    if request.method == 'POST':
        loom = login(request.POST)

        if loom.is_valid():
            una = request.POST.get('username')
            pwd = request.POST.get('password')
            if register.objects.filter(username=una):

                user = register.objects.filter(username=una, password=pwd)
                if user:
                    return HttpResponse('login success')
                else:
                    messages.warning(request, 'Invalid credentials')
                    return render(request, 'login.html', {'form': loom})
            else:
                user = register.objects.filter(mobile=una, password=pwd)
                if user:
                    return HttpResponse('login success')
                else:
                    messages.warning(request, 'Invalid credentials')
                    return render(request, 'login.html')
        else:
            loom = login()
            return render(request, 'login.html', context={'form': loom})
    else:
        loom = login()
        return render(request, 'login.html', context={'form': loom})
