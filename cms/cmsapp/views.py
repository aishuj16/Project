from django.shortcuts import render, redirect
from .models import dModel,sModel
from .forms import dForm,sForm


def home(request):
	return render (request, "home.html")


def dept(request):
	data = dModel.objects.all()
	return render (request, "dept.html" , {"data":data})


def Adept(request):
	if request.method=="POST":
		data=dForm(request.POST)
		if data.is_valid():
			data.save()
			fm=dForm
			return render (request, "Adept.html", {"fm":fm, "msg":"Department Added"})
		else:
			return render (request, "Adept.html", {"fm":data, "msg":"Error"})
	else:
		fm=dForm
		return render (request, "Adept.html", {"fm":fm})

def remove(request , d):
	dt= dModel.objects.get(did=d)
	dt.delete()
	return redirect("dept")


def std(request):
	data = sModel.objects.all()
	return render (request, "std.html" , {"data":data})


def Astd(request):
	if request.method=="POST":
		data=sForm(request.POST)
		if data.is_valid():
			data.save()
			fm=sForm
			return render (request, "Astd.html", {"fm":fm, "msg":"Student Added"})
		else:
			return render (request, "Astd.html", {"fm":data, "msg":"Error"})
	else:
		fm=sForm
		return render (request, "Astd.html", {"fm":fm})

def dele(request , s):
	st= sModel.objects.get(rno =s)
	st.delete()
	return redirect("std")
	