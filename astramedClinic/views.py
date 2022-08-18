from django.shortcuts import render

from astramedClinic.models import Services, Employee, Reviews, Blog, UnderServices, MainModel


def main(request):
    services = Services.objects.all()[:6]
    blog = Blog.objects.order_by("?")[:3]
    mainObjects = MainModel.objects.all()
    reviews = Reviews.objects.all()
    data = {
        'services': services,
        'blog': blog,
        'mainObjects': mainObjects,
        'reviews': reviews
    }
    return render(request, 'main/index.html', data)


def about(request):
    services = Services.objects.order_by("?")[:3]

    data = {
        'services': services,
    }
    return render(request, 'main/about.html', data)


def authorization(request):
    return render(request, 'main/authorization.html')


def blog(request):
    blogs = Blog.objects.all()
    fresh = Blog.objects.order_by("-id")[:3]
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
    recomended_blogs = Blog.objects.order_by("?")[:3]

    data = {
        'blogs': blogs,
        'recomended_blogs': recomended_blogs
    }
    return render(request, 'main/post.html', data)


def procedure(request, pk):
    services = UnderServices.objects.filter(id=pk)
    recomended_services = Services.objects.order_by("?")[:3]
    data = {
        'services': services,
        'recomended_services': recomended_services,
    }
    return render(request, 'main/procedure.html', data)


def profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

    recomended_services = Services.objects.order_by("-pk")[:3]

    data = {
        'recomended_services': recomended_services,
    }
    return render(request, 'main/profile.html', data)


def registration(request):
    return render(request, 'main/registration.html')


def review(request):
    reviews = Reviews.objects.filter(published=True)
    services = Services.objects.order_by("?")[:3]

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
    recomended_blogs = Blog.objects.order_by("?")[:3]

    data = {
        'employes': employes,
        'recomended_blogs': recomended_blogs,
    }
    return render(request, 'main/team.html', data)


def therapy(request, pk):
    services = Services.objects.filter(id=pk)
    recomended_services = Services.objects.order_by("?")[:3]
    underServices = UnderServices.objects.filter(maintype_id=pk)
    data = {
        'services': services,
        'recomended_services': recomended_services,
        'underServices': underServices
    }
    return render(request, 'main/therapy.html', data)


def thanks(request):
    return render(request, 'main/thanks.html')


def all_info(request):
    return render(request, 'main/all_info.html')


def info(request):
    return render(request, 'main/info.html')
