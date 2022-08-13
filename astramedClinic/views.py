from django.shortcuts import render

from astramedClinic.models import Services, Employee, Reviews, Blog


def main(request):
    services = Services.objects.all()[:6]
    blog = Blog.objects.all()[:3]

    data = {
        'services': services,
        'blog': blog,
    }
    return render(request, 'main/index.html', data)


def about(request):
    services = Services.objects.all()[:3]

    data = {
        'services': services,
    }
    return render(request, 'main/about.html', data)


def authorization(request):
    return render(request, 'main/authorization.html')


def blog(request):
    blogs = Blog.objects.all()
    fresh = Blog.objects.order_by("-pk")[:3]
    data = {
        'blogs': blogs,
        'fresh': fresh,
    }
    return render(request, 'main/blog.html', data)


def contacts(request):
    return render(request, 'main/contacts.html')


def member(request, employee_name):
    employes = Employee.objects.filter(name=employee_name)
    data = {
        'employes': employes
    }
    return render(request, 'main/member.html', data)


def post(request, blog_title):
    blogs = Blog.objects.filter(title=blog_title)
    recomended_blogs = Blog.objects.all()[:3]

    data = {
        'blogs': blogs,
        'recomended_blogs': recomended_blogs
    }
    return render(request, 'main/post.html', data)


def procedure(request, pk):
    services = Services.objects.filter(id=pk)
    print(services)
    data = {
        'services': services
    }
    return render(request, 'main/procedure.html', data)


def profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

    return render(request, 'main/profile.html')


def registration(request):
    return render(request, 'main/registration.html')


def review(request):
    reviews = Reviews.objects.filter(published=True)
    services = Services.objects.all()[:3]
    print(request.user)
    data = {
        'services': services,
        'reviews': reviews
    }
    return render(request, 'main/review.html', data)


def services(request):
    services = Services.objects.all()

    data = {
        'services': services,
    }

    return render(request, 'main/services.html', data)


def team(request):
    employes = Employee.objects.all()
    data = {
        'employes': employes
    }
    return render(request, 'main/team.html', data)


def therapy(request):
    return render(request, 'main/therapy.html')


def thanks(request):
    return render(request, 'main/thanks.html')