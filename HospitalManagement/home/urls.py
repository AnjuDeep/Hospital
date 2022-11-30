from django.urls import path

from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('booking/', views.booking,name='booking'),
    path('doctors/', views.doctors,name='doctors'),
    path('department/', views.department,name='department'),
    path('gallery/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
    path('saveenquiry/', views.saveEnquiry,name='saveenquiry'),

    path('careers/', views.careers,name='careers'),
    path('careers/openings/', views.openings),
    path('insurance/', views.insurance,name='insurance'),
    path('checkup/', views.checkup,name='checkup'),
    path('treatment/', views.treatment,name='treatment'),

    path('anaesthesiology/', views.anaesthesiology,name='anaesthesiology'),
    path('breast/', views.breast,name='breast'),
    path('cardiology/', views.cardiology,name='cardiology'),
    path('critical/', views.critical,name='critical'),
    path('dermatology/', views.dermatology,name='dermatology'),
    path('emergency/', views.emergency,name='emergency'),
    path('ent/', views.ent,name='ent'),
    path('nephrology/', views.nephrology,name='nephrology'),
    path('neurology/', views.neurology,name='neurology'),
    path('ophthalmology/', views.ophthalmology,name='ophthalmology'),
    path('paediatrics/', views.paediatrics,name='paediatrics'),
    path('urology/', views.urology,name='urology')
]
