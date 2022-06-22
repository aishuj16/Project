from django.db import models

class Customer(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=500)


    def register(self):
        self.save()

    def get_customer_by_email(email):
        return Customer.objects.get(email = email)


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False