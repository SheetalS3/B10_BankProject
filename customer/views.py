from django.shortcuts import render,HttpResponse, redirect
from .models import Customer

# Create your views here.

def homepage(request):
    all_cust= Customer.objects.all()
    return render(request, "home.html", {'all_cust': all_cust})

def add_new_customer(request):
    all_branches = Customer.BRANCHES
    if not request.POST.get('html_id'):
        if request.method == 'POST':
            Customer.objects.create(first_name= request.POST.get('html_fname'),last_name= request.POST.get('html_lname'),
                                    account_id= request.POST.get('html_accID'),registration_date= request.POST.get('html_date'),
                                    branch_name= request.POST.get('html_branches'), gender= request.POST.get('html_gender'))
            return redirect('home')
        elif request.method == 'GET':
            return render(request, "add_customer.html", {'all_branches': all_branches})
    else:
        update_cust = Customer.objects.get(id= (request.POST.get('html_id')))
        update_cust.first_name= request.POST.get('html_fname')
        update_cust.last_name= request.POST.get('html_lname')
        update_cust.account_id= request.POST.get('html_accID')
        update_cust.registration_date= request.POST.get('html_date')
        update_cust.branch_name= request.POST.get('html_branches')
        update_cust.gender= request.POST.get('html_gender')
        update_cust.save()
        return redirect('home')

def delete_customer(request, c_id):
    try:
        del_cust = Customer.objects.get(id = c_id)
    except Customer.DoesNotExist:  
        return HttpResponse("Customer record does not exist")  
    else:    
        if request.POST.get("html_hard_delete") == "hard_delete":
            del_cust.delete()
            return redirect('show_del_customers')
        else:        
            del_cust.is_deleted = True
            del_cust.save()
            return redirect('home')


def show_del_customers(request):
    del_customers = Customer.objects.filter(is_deleted= True)
    return render(request, "show_del_customers.html", {'del_customers': del_customers})

def restore_customers(request, c_id):
    res_cust = Customer.objects.get(id= c_id)
    res_cust.is_deleted = False
    res_cust.save()
    return redirect('home')

def update_customer(request, c_id):
    try:
        update_cust = Customer.objects.get(id= c_id)
    except Customer.DoesNotExist:
        return HttpResponse("Customer record does not exist...")
    else:
        return render(request, 'add_customer.html', {'update_cust':update_cust})

'''--------------------REST API testing--------------------- '''
import requests

GET_SINGLE_STUD_URL = "http://127.0.0.1:8000/api/get-student/{}"
GET_ALL_STUDS_URL = "http://127.0.0.1:8000/api/get-all-student"
CREATE_STUD_URL = "http://127.0.0.1:8000/api/create-student"

def get_single_stud(request, id):
    response = requests.get(GET_SINGLE_STUD_URL.format(id))
    python_dict= response.json()
    return render(request, "student_api.html", {"data": python_dict})

def get_all_students(request):
    response = requests.request('GET', GET_ALL_STUDS_URL)
    python_dict = response.json() # json to python dict
    return render(request, "student_api.html", {"all_data": python_dict})







'''------------------------------------------------------------'''    
# {% %}  remember % sign
# request.post.get('') remember get("") ahe
# hard delete ch button ahe but tyavar aplyala value ani name pan dyaychay ani url pan mention karaychi ahe tar
#                <form method="POST" action="{% url 'delete_customer' customer.id %}">
                #     {% csrf_token %}
                #     <input type="hidden" name="html_hard_delete" value="hard_delete">
                #     <button type="submit">Hard Delete</button>
                # </form>
    
# if request.POST.get("html_hard_delete") == "hard_delete":
#                        name                    value
    
# except Customer.DoesNotExist:  
#        return HttpResponse("Customer record does not exist")     

# in update_customer view....return redirecr nahi tar return render karaychay


