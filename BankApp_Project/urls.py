"""BankApp_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer.views import homepage, add_new_customer, delete_customer, show_del_customers, restore_customers, update_customer,get_single_stud, get_all_students


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name= 'home'),
    path('add/', add_new_customer, name= 'add_new_customer'),
    path('delete/<int:c_id>', delete_customer, name= 'delete_customer'),
    path('show_deleted/', show_del_customers, name= 'show_del_customers'),
    path('restore/<int:c_id>', restore_customers, name= 'restore_customers'),
    path('update/<int:c_id>', update_customer, name= 'update_customer'),
    path('get-student/<int:id>', get_single_stud),                        #APT test URL
    path('get-all-students/', get_all_students), 
]

