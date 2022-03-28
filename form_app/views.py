from django.shortcuts import render
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
    return render(request,"show.html", context)
    