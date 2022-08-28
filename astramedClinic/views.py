from __future__ import print_function

import base64
from email.message import EmailMessage

import requests
from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from astramedClinic.config import gmail_send_message
from astramedClinic.models import Services, Employee, Reviews, Blog, UnderServices, MainModel, Info, Applications, Jobs, Partners, PriceList


def main(request):
    services = Services.objects.all()[:6]
    blog = Blog.objects.order_by("?")[:3]
    mainObjects = MainModel.objects.all()
    reviews = Reviews.objects.filter(published=True)
    print(reviews)
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


def post(request, pk):
    blogs = Blog.objects.filter(pk=pk)
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
    except:
        pass
    return render(request, 'main/order.html', data)


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
    path = str(request.META.get('HTTP_REFERER'))
    if request.method == 'POST':
        if 'order' in path:
            name = request.POST.get('LFname')
            birth = request.POST.get('birth')
            address = request.POST.get('address')
            therapy = request.POST.get('therapy')
            number = request.POST.get('number')
            Applications.objects.create(name=name, birth=birth, address=address, therapy=therapy, number=number)
            method = 'https://api.telegram.org/bot5684471230:AAF6eLJajz0Rj7Ksjzy3uKbWnGQRb5HC-SQ/sendMessage'
            text = f'ФИО: {name}\n' \
                   f'Дата рождения: {birth}\n' \
                   f'Адрес: {address}\n' \
                   f'Терапия: {therapy}\n' \
                   f'Номер: {number}',
            requests.post(method, data={
                'chat_id': 1600170280,
                'text': text
            })

            # creds = gmail_send_message()
            # try:
            #     service = build('gmail', 'v1', credentials=creds)
            #     message = EmailMessage()
            #
            #     message.set_content(f'ФИО: {name}\n' \
            #                         f'Дата рождения: {birth}\n' \
            #                         f'Адрес: {address}\n' \
            #                         f'Терапия: {therapy}\n' \
            #                         f'Номер: {number}')
            #
            #     message['To'] = 'bear.lvb@gmail.com'
            #     message['From'] = 'DekontFarmBot@gmail.com'
            #     message['Subject'] = 'Automated draft'
            #
            #     # encoded message
            #
            #     encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            #         .decode()
            #     create_message = {
            #         'raw': encoded_message
            #     }
            #     # pylint: disable=E1101
            #     send_message = (service.users().messages().send
            #                     (userId="me", body=create_message).execute())
            #     print(F'Message Id: {send_message["id"]}')
            # except HttpError as error:
            #     print(F'An error occurred: {error}')
            #     send_message = None

        if 'review' in path:
            name = request.POST.get('name')
            description = request.POST.get('description')
            Reviews.objects.create(name=name, description=description)
            method = 'https://api.telegram.org/bot5684471230:AAF6eLJajz0Rj7Ksjzy3uKbWnGQRb5HC-SQ/sendMessage'
            text = f'ФИО: {name}\n' \
                   f'Отзыв: {description}\n'
            requests.post(method, data={
                'chat_id': 1600170280,
                'text': text
            })
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
    data = {
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
    print(price.values('priceFile'))
    return render(request, 'main/priceList.html', data)
