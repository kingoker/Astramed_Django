from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('about/', views.about, name='about'),
    path('authorization/', views.authorization, name='authorization'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contacts, name='contacts'),
    path('member/<employee_name>', views.member, name='member'),
    path('post/<blog_title>', views.post, name='post'),
    path('procedure/<pk>', views.procedure, name='procedure'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('review/', views.review, name='review'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('therapy/<pk>', views.therapy, name='therapy'),
    path('thanks/', views.thanks, name='thanks'),
    path('all_info/', views.all_info, name='all_info'),
    path('info/<str>', views.info, name='info'),
]