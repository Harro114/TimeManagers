from django.shortcuts import render


# Create your views here.
def task_list(requests):
    return render(requests, "timeAllocator/index.html")


def registration(request):
    return render(request, "timeAllocator/registration.html")