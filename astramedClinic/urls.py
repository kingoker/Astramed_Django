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
    path('member/<str>', views.member, name='member'),
    path('post/', views.post, name='post'),
    path('procedure/<pk>', views.procedure, name='procedure'),
    path('profile/', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('review/', views.review, name='review'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('therapy/', views.therapy, name='therapy'),

]