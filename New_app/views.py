from django.shortcuts import render, redirect 
from . import views
from .models import *
from django.contrib import messages 
import bcrypt

def index(request):
    return  render (request, "index.html")


def register(request):
    print("making new user")
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/TheRift')
    else:
        if request.method=="POST":
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            create_user = User.objects.create(first_name= request.POST["first_name"], last_name= request.POST["last_name"], user_name = request.POST["user_name"], email=request.POST["email"], password=pw_hash)
            request.session['user_id']= create_user.id
            create_user.save()
            return redirect('/league')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user)!= 0:
        if bcrypt.checkpw(request.POST['password'].encode(),user[0].password.encode()):
            user= user[0]
            request.session['user_id']= user.id
            return redirect("/league")
    messages.warning(request, "Invalid Log In")
    return redirect('/TheRift')

def league(request):
    context ={
        "user": User.objects.get(id=request.session['user_id'])
}
    return render(request, "league.html",context)


def top(request):
    context={
        "user": User.objects.get(id=request.session['user_id']),
        "paths":Path.objects.all(),
        "messages": Message.objects.all()

    }
    return render(request, "top.html", context)

def mid(request): 
    context={
        "user": User.objects.get(id= request.session['user_id']),
        "paths":Path.objects.all(),
        "messages": Message.objects.all()
    }
    return render(request, "mid.html", context)

def jungle(request): 
    context={
        "user": User.objects.get(id= request.session['user_id']),
        "paths":Path.objects.all(),
        "messages": Message.objects.all()

    }
    return render(request, "jungle.html", context)


def adc(request): 
    context={
        "user": User.objects.get(id= request.session['user_id']),
        "paths":Path.objects.all(),
        "messages": Message.objects.all()

    }
    return render(request, "adc.html", context)

def support(request): 
    context={
        "user": User.objects.get(id= request.session['user_id']),
        "paths":Path.objects.all(),
        "messages": Message.objects.all()

    }
    return render(request, "support.html", context)

def go_back(request):
    return redirect('/league')


def builder(request):
    user_id =User.objects.get(id=request.session['user_id'])
    context ={
        "user_id": User.objects.get(id=request.session['user_id']),
        "user_path": Path.objects.filter(user_upload = user_id),
        "paths": Path.objects.all()
    }
    return render(request, "builder.html", context)


def path_build(request):
    if request.session['user_id']:
        title = request.POST['title']
        champion = request.POST['champion']
        build = request.POST['build']
        lane = request.POST['lane']
        user = User.objects.get(id= request.session['user_id'])
        path = Path.objects.create(title = title, champion=champion, lane=lane, build=build, user_upload = user)
        return redirect('/top')


def comment(request):
        Message.objects.create(message=request.POST['message'], user= User.objects.get(id=request.session['user_id']))
        return redirect('/top')



def logout(request):
    request.session.clear()
    return redirect('/TheRift')


