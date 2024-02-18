from django.db import models

# Create your models here.

class CustomerManager(models.Manager):
    def get_deleted_customers(self):
        return self.filter(is_deleted= True)
    
    def get_active_customers(self):
        return self.filter(is_deleted= False)

class Customer(models.Model):
    BRANCHES = [
        ('Baner', 'Baner'),
        ('Katraj', 'Katraj'),
        ('Pimpari', 'Pimpari'),
        ('Bavdhan', 'Bavdhan')
    ]

    GENDER= [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length= 200)
    account_id = models.IntegerField(default= 6327637)
    registration_date = models.DateField()
    is_deleted= models.BooleanField(default= False)
    branch_name= models.CharField(max_length= 20, choices= BRANCHES, null=True)
    gender = models.CharField(max_length= 5, choices= GENDER, null= True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'customer_db'

class BankBranch(models.Model):
    branch_name= models.CharField(max_length= 200)
    branch_id = models.IntegerField()
    customer= models.OneToOneField(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.branch_name}"

class Address(models.Model):
    state= models.CharField(max_length= 100)
    city= models.CharField(max_length= 100)
    pincode= models.IntegerField()
    customer= models.ForeignKey(Customer, on_delete= models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.state} {self.city}"

