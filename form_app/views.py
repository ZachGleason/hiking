from django.shortcuts import render
from form_app.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def create_user(request):
    template = 'reg_form.html'
    print("Got Post Info....................")
    first_name = request.POST.get['first_name']
    last_name = request.POST.get['last_name']
    email= request.POST.get['email']
    password = request.POST.get['password']
    context = {
        "first" : first_name,
        "last" : last_name,
        "mail" : email,
        "pass" : password,
    }
    print(first_name)
    print(last_name)
    print(email)
    print(password)
    return render(request, template, context)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="reg_form.html", context={"register_form":form})