from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_member, name='add_member'),
    path('view/', views.view_members, name='view_members'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('disable/<int:member_id>/', views.disable_member, name='disable_member'),
    path('export/excel/', views.export_members_excel, name='export_members_excel'),
    path('export/pdf/', views.export_members_pdf, name='export_members_pdf'),
]
