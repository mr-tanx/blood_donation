# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),
    path("adminlogout",views.logout,name="adminlogout"),
    path("donor",views.donor_view,name="donor"),  # Updated to donor_view
    path("recipient", views.recipient_view, name="recipient"),  # Updated to recipient_view
    path("donoradd",views.donoradd,name="donoradd"),
    path("recipientadd",views.recipientadd,name="recipientadd"),
    path("crud",views.crud,name="crud"),
    path('add_donor/', views.add_donor, name='add_donor'),
    path('delete_donor/', views.delete_donor, name='delete_donor'),
    path('update_donor/', views.update_donor, name='update_donor'),
    path('search_donor/', views.search_donor, name='search_donor'),

  ]
