from django.shortcuts import render

# Create your views here.
from astramedClinic.models import Services, Employee, Reviews


def main(request):
    services = Services.objects.all()[:6]
    data = {
        'services': services
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def authorization(request):
    return render(request, 'main/authorization.html')


def blog(request):
    return render(request, 'main/blog.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def member(request, str):
    employes = Employee.objects.filter(name=str)
    data = {
        'employes': employes
    }
    return render(request, 'main/member.html', data)


def post(request):
    return render(request, 'main/post.html')


def procedure(request, pk):
    services = Services.objects.filter(id=pk)
    print(services)
    data = {
        'services': services
    }
    return render(request, 'main/procedure.html', data)


def profile(request):
    return render(request, 'main/profile.html')


def registration(request):
    return render(request, 'main/registration.html')


def review(request):
    reviews = Reviews.objects.filter(published=True)
    services = Services.objects.all()[:3]
    data = {
        'services': services,
        'reviews': reviews
    }
    return render(request, 'main/review.html', data)


def services(request):
    return render(request, 'main/services.html')


def team(request):
    employes = Employee.objects.all()
    data = {
        'employes': employes
    }
    return render(request, 'main/team.html', data)


def therapy(request):
    return render(request, 'main/therapy.html')
