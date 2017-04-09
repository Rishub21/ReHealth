from django.conf.urls import patterns, url
from compliance import views

urlpatterns = patterns( "" ,
        url(r'^$', views.index, name='index'),
        url(r'^doctor_Registration/', views.doctor_Registration, name='doctor_Registration'),
        url(r'^patient_Registration/', views.patient_Registration, name='patient_Registration'),
        url(r'^initial_Registration/', views.initial_Registration, name='initial_Registration'),
        url(r'^patient_Dashboard/(?P<patient_name>[\w\-"]+)/$', views.patient_Dashboard, name='patient_Dashboard'),
        url(r'^doctor_feedback/', views.doctor_feedback, name='doctor_feedback'),
        url(r'^doctor_Login/', views.doctor_Login, name='doctor_Login'),
        url(r'^initial_Dashboard/', views.initial_Dashboard, name='initial_Dashboard'),



)
