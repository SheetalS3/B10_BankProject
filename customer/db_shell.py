# exec(open(r"D:\Sheetal\Python\Scripting files\Django_Projects\BankApp_Project\customer\db_shell.py").read())

from customer.models import Customer, BankBranch, Address

# cust= Customer(first_name= "Minal", last_name= "Joshi", email= 'minal@gmail.com',registration_date= '2023-7-12')
# cust.save()

# Customer.objects.create(first_name= "Ankita", last_name= "Doghe", email= 'ankita@gmail.com',registration_date= '2020-5-28')
# Customer.objects.create(first_name= "Nilima", last_name= "Bhide", email= 'nilima@gmail.com',registration_date= '1999-5-2')
# Customer.objects.create(first_name= "Monali", last_name= "Shende", email= 'monali@gmail.com',registration_date= '1989-8-20')

# all_cust = Customer.objects.all()
# for cust in all_cust:
#     print(cust.first_name)

# c1 = Customer.objects.get(first_name= 'Minal')
# c1.account_id = 562251265
# c1.save()

# c2 = Customer.objects.get(first_name= 'Ankita')
# c2.account_id = 72787728
# c2.save()

# c3 = Customer.objects.get(first_name= 'Nilima')
# c3.account_id = 6887879
# c3.save()

'''-------One to one-------'''
c1 = Customer.objects.get(first_name= 'Minal')
c2 = Customer.objects.get(first_name= 'Ankita')
c3 = Customer.objects.get(first_name= 'Nilima')

# BankBranch.objects.create(branch_name="Ambegoan" , branch_id= 76, customer= c1)
# BankBranch.objects.create(branch_name="Katraj" , branch_id= 76, customer_id= c2.id)
# BankBranch.objects.create(branch_name="Baner" , branch_id= 76, customer= c3)

# b1= BankBranch.objects.get(id= 1)
# print(b1.customer)

'''----One to many-----'''

# Address.objects.create(state= "MH", city= "Pune", pincode= "410045", customer= c1)
# Address.objects.create(state= "KN", city= "Mumbai", pincode= "410677", customer= c1)
# Address.objects.create(state= "JK", city= "Delhi", pincode= "877045", customer= c2)
# Address.objects.create(state= "TN", city= "Chennai", pincode= "6770045", customer= c2)

# a1 = Address.objects.filter(customer= c1)
# print(a1)

# multi_a = Address.objects.filter(id__in = [9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]).delete()

# a1 = Address.objects.filter(customer= c1).update(customer= c3)
















