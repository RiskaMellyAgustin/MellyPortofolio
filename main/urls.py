from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/revenue/', views.project_revenue, name='project_revenue'),
    path('projects/dropout/', views.project_dropout, name='project_dropout'),
    path('projects/dormitory/', views.project_dormitory, name='project_dormitory'),
    path('projects/puma/', views.project_puma, name='project_puma'),
    path('projects/looker/', views.project_looker, name='project_looker'),

    # path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
