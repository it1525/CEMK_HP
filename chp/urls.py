from django.urls import path
from . import views as c_views

urlpatterns= [
path('',c_views.homepage,name='home'),
path('about',c_views.about,name='about'),
path('dept',c_views.dept,name='dept'),
path('Adcomplain',c_views.Adcomplain,name='Adcomplain'),
path('Acomplain',c_views.Acomplain,name='Acomplain'),
path('Ccomplain',c_views.Ccomplain,name='Ccomplain'),
path('Ecomplain',c_views.Ecomplain,name='Ecomplain'),
path('Mcomplain',c_views.Mcomplain,name='Mcomplain'),
path('Scomplain',c_views.Scomplain,name='Scomplain'),
path('Rcomplain',c_views.Rcomplain,name='Rcomplain'),
path('checkallcomplain',c_views.checkallcomplain,name='checkallcomplain'),
path('checkyourcomplain',c_views.checkyourcomplain,name='checkyourcomplain'),
path('checkdeptcomplain',c_views.DeptComplainListView.as_view(),name='checkdeptcomplain'),
path('complain/<int:pk>/update/',c_views.ComplainUpdateView.as_view(), name='complain-update'),
path('user-detail/<str:username>',c_views.user_detail,name='user-detail'),
path('thank',c_views.thank,name='thank'),
];
