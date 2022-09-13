from __future__ import print_function
import random
import base64
from email.message import EmailMessage

import requests
from django.core.mail import send_mail
from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.http import HttpResponseRedirect

from astramedClinic.config import gmail_send_message
from astramedClinic.models import Services, Employee, Reviews, Blog, UnderServices, MainPage, Info, Applications, Jobs, \
    Partners, PriceList, Links, Contacs, AboutPage, CooperationPage, PhilosBlog, ServicesPage


admins = [1600170280, 938759596, ]


def sendMessage(text, *args):
    method = 'https://api.telegram.org/bot5684471230:AAF6eLJajz0Rj7Ksjzy3uKbWnGQRb5HC-SQ/sendMessage'
    for chat_id in args[0]:
        print(chat_id)
        requests.post(method, data={
            'chat_id': chat_id,
            'text': text
        })


def sendDocument(text, file, *args):
    method = 'https://api.telegram.org/bot5684471230:AAF6eLJajz0Rj7Ksjzy3uKbWnGQRb5HC-SQ/sendDocument'
    files = {"document": file}
    title = text
    for chat_id in args[0]:
        requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)


def main(request):
    services = Services.objects.all()[:6]
    items = list(Blog.objects.all())
    blog = random.sample(items, 3)
    mainObjects = MainPage.objects.all()
    reviews = Reviews.objects.filter(published=True)
    data = {
        'services': services,
        'blog': blog,
        'mainObjects': mainObjects,
        'reviews': reviews
    }

    # Код для отправки емейла
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'temp@astramed-clinic.com',
    #     ['bear.lvvb@mail.ru'],
    #     fail_silently=False,
    # )

    return render(request, 'main/index.html', data)


def about(request):
    items = list(Services.objects.all())
    reviews = Reviews.objects.filter(published=True)
    services = random.sample(items, 3)
    aboutPage = AboutPage.objects.all()
    philosopies = PhilosBlog.objects.all()

    data = {
        'services': services,
        'aboutPage': aboutPage,
        'philosopies': philosopies,
        'reviews': reviews
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
    contacts = Contacs.objects.all()
    links = Links.objects.all()
    print(links.values())
    data = {
        'contacts': contacts,
        'links': links,
    }
    return render(request, 'main/contacts.html', data)


def member(request, employee_name):
    employes = Employee.objects.filter(name=employee_name)
    review_list = Reviews.objects.filter(doctor=employee_name)
    data = {
        'employes': employes,
        'review_list': review_list
    }
    return render(request, 'main/member.html', data)


def post(request, pk):
    blogs = Blog.objects.filter(pk=pk)
    items = list(Blog.objects.all())
    recomended_blogs = random.sample(items, 3)

    data = {
        'blogs': blogs,
        'recomended_blogs': recomended_blogs
    }
    return render(request, 'main/post.html', data)


def procedure(request, pk):
    services = UnderServices.objects.filter(id=pk)
    items = list(Services.objects.all())
    recomended_services = random.sample(items, 3)
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


def order(request, pk):
    path = str(request.META.get('HTTP_REFERER'))
    data = {
        'services': ['Записаться на консультацию']
    }
    try:
        if "therapy" in path:
            services = Services.objects.filter(pk=pk)
            data = {
                'services': [services.values('type')[0]['type']]
            }
        elif "procedure" in path:
            services = UnderServices.objects.filter(pk=pk)
            data = {
                'services': [services.values('undertype')[0]['undertype']]
            }
        elif "member" in path:
            member = Employee.objects.filter(pk=pk)
            print(member)
            data = {
                'member': [member.values('name')[0]['name']]
            }
    except:
        pass
    return render(request, 'main/order.html', data)


def review(request):
    reviews = Reviews.objects.filter(published=True)
    items = list(Services.objects.all())
    services = random.sample(items, 3)
    data = {
        'services': services,
        'reviews': reviews
    }
    return render(request, 'main/review.html', data)


def services(request):
    services = Services.objects.all()
    servicePage = ServicesPage.objects.all()
    data = {
        'services': services,
        'servicePage': servicePage
    }

    return render(request, 'main/services.html', data)


def team(request):
    employes = Employee.objects.all()
    items = list(Blog.objects.all())
    recomended_blogs = random.sample(items, 3)
    data = {
        'employes': employes,
        'recomended_blogs': recomended_blogs,
    }
    return render(request, 'main/team.html', data)


def therapy(request, pk):
    services = Services.objects.filter(id=pk)
    items = list(Services.objects.all())
    print(services.values())
    recomended_services = random.sample(items, 3)
    underServices = UnderServices.objects.filter(maintype_id=pk)
    data = {
        'services': services,
        'recomended_services': recomended_services,
        'underServices': underServices
    }
    return render(request, 'main/therapy.html', data)


def thanks(request):
    path = str(request.META.get('HTTP_REFERER'))

    if request.method == 'POST':
        if 'order' in path:
            name = request.POST.get('LFname')
            birth = request.POST.get('birth')
            address = request.POST.get('address')
            therapy=""
            doctor=""
            number = request.POST.get('number')
            if request.POST.get('therapy'):
                therapy = request.POST.get('therapy')
                text = f'Запись на прием: {therapy}\n' \
                       f'ФИО: {name}\n' \
                       f'Дата рождения: {birth}\n' \
                       f'Адрес: {address}\n' \
                       f'Терапия: {therapy}\n' \
                       f'Номер: {number}\n',
            elif request.POST.get('doctor'):
                doctor = request.POST.get('doctor')
                text = f'Запись к врачу: {doctor}\n' \
                       f'ФИО: {name}\n' \
                       f'Дата рождения: {birth}\n' \
                       f'Адрес: {address}\n' \
                       f'Терапия: {therapy}\n' \
                       f'Номер: {number}\n',
            else:
                text = f'Запись на консультацию\n' \
                       f'ФИО: {name}\n' \
                       f'Дата рождения: {birth}\n' \
                       f'Адрес: {address}\n' \
                       f'Номер: {number}\n',
            Applications.objects.create(name=name, birth=birth, address=address, therapy=therapy, number=number, doctor=doctor)
            sendMessage(text, admins)

        elif 'review' in path or 'member' in path:
            name = request.POST.get('name')
            description = request.POST.get('description')
            doctor = ""
            print(request.POST.get('doctor'))
            if 'member' in path:
                doctor = request.POST.get('doctor')
            Reviews.objects.create(name=name, description=description, doctor=doctor)
            text = f'ФИО: {name}\n' \
                   f'Отзыв: {description}\n'
            sendMessage(text, admins)
            if 'member' in path:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        elif 'jobOffer' in path:
            name = request.POST.get('LFname')
            number = request.POST.get('number')
            address = request.POST.get('address')
            therapy = request.POST.get('therapy')
            text = f'Вакансия: {therapy}' \
                   f'ФИО: {name}\n' \
                   f'Номер: {number}\n' \
                   f'Адрес: {address}'
            sendDocument(text, request.FILES['resume'], admins)

        if 'about' in path or 'blog' in path or 'contacts' in path or 'index' in path or 'services' in path:
            name = request.POST.get('name')
            phone = request.POST.get('phone')

            text = f'Просьба позвонить:' \
                   f'ФИО: {name}\n' \
                   f'Номер: {phone}\n'
            sendMessage(text, admins)
        if 'partner' in path:
            componyName = request.POST.get('componyName')
            email = request.POST.get('email')
            number = request.POST.get('number')
            url = request.POST.get('url')

            text = f'Заявка в партнеры:' \
                   f'Компанмя:: {componyName}\n' \
                   f'Почта: {email}\n' \
                   f'Номер: {number}\n' \
                   f'Ссылка: {url}\n'
            sendMessage(text, admins)
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     'temp@astramed-clinic.com',
            #     ['bear.lvvb@mail.ru'],
            #     fail_silently=False,
            # )
    return render(request, 'main/thanks.html')


def all_info(request):
    all_info = Info.objects.all()
    data = {
        'all_info': all_info
    }
    return render(request, 'main/all_info.html', data)


def info(request, str):
    current_info = Info.objects.filter(title=str)
    data = {
        'current_info': current_info,
    }
    return render(request, 'main/info.html', data)


def cooperation(request):
    jobs = Jobs.objects.all()
    partners = Partners.objects.all()
    cooperationPage = CooperationPage.objects.all()

    data = {
        'cooperationPage': cooperationPage,
        'jobs': jobs,
        'partners': partners
    }
    return render(request, 'main/cooperation.html', data)


def offer(request,job):
    jobs = Jobs.objects.filter(title=job)
    data = {
        'jobs': jobs,
    }
    return render(request, 'main/jobOffer.html', data)


def priceList(request):
    price = PriceList.objects.all()
    data = {
        'price': price,
    }
    return render(request, 'main/priceList.html', data)


def base(request):
    contacts = Contacs.objects.all()
    links = Links.objects.all()
    data = {
        'contacts': contacts,
        'links': links,
    }
    return data


def search(request):
    if request.method == "POST":
        print(request.POST)
        searched = request.POST['searched']
        blog_list = Blog.objects.filter(title__iregex=rf'({searched})')
        print(blog_list)
        services_list = Services.objects.filter(type__iregex=rf'({searched})')
        underservices_list = UnderServices.objects.filter(undertype__iregex=rf'({searched})')
        return render(request, 'main/result.html', {'blog_list': blog_list, 'services_list': services_list, 'underservices_list': underservices_list})
    else:
        return render(request, 'main/result.html', {})


def partner(request):
    return render(request, 'main/partnerRegistration.html')
