from django.shortcuts import render

# Create your views here.
from astramedClinic.models import Services


def main(request):
    services = Services.objects.all()
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


def member(request):
    return render(request, 'main/member.html')


def post(request):
    return render(request, 'main/post.html')


def procedure(request, str):
    return render(request, 'main/procedure.html')


def profile(request):
    return render(request, 'main/profile.html')


def registration(request):
    return render(request, 'main/registration.html')


def review(request):
    return render(request, 'main/review.html')


def services(request):
    return render(request, 'main/services.html')


def team(request):
    return render(request, 'main/team.html')


def therapy(request):
    return render(request, 'main/therapy.html')
