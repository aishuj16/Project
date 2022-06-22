from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self , request):
        return render(request, "signup.html")

    def post(self , request):
        postData = request.POST
        fname = postData.get('fname')
        lname = postData.get('lname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('pass')

        value = {'fname': fname,
                 'lname': lname,
                 'phone': phone,
                 'email': email
                 }
        customer = Customer(fname=fname,
                            lname=lname,
                            phone=phone,
                            email=email,
                            password=password)

        error = self.validate(customer)

        # saving
        if (not error):
            print(fname, lname, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("index")
        else:
            data = {
                'error': error,
                'values': value
            }
            return render(request, "signup.html", data)


    def validate(self , customer):
        error = None
        if (not customer.fname):
            error = "First Name is Required"
        elif len(customer.fname) < 4:
            error = "Name must be 4 charcater long"
        elif (not customer.lname):
            error = "Last Name is Required"
        elif len(customer.lname) < 4:
            error = "Name must be 4 charcater long"
        elif (not customer.phone):
            error = "Phone Number  is Required"
        elif len(customer.phone) < 10:
            error = "Phone number must have 10 digit"
        elif (not customer.password):
            error = "Password is Required"
        elif len(customer.password) < 8:
            error = "Password must be 8 charcater long"

        elif customer.isExists():
            error = "Email is already registered"

        return error