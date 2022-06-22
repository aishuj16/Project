from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.views import View


class Login(View):
    def get(self , request):
        return render(request, "login.html")
    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('pass')
        customer = Customer.get_customer_by_email(email)
        value = {'email': email}
        error = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                return redirect("index")
            else:
                error = "Email or password is invalid !! "
        else:
            error = "Email or password is invalid !! "

        return render(request, "login.html", {'error': error})