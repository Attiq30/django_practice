from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
def nasir(request):
  return HttpResponse('name is attiq')

def home (request):
  d={"name":"attiq ur rehman",
     "roll_no": "123"}
  return render (request, "course/home.html", d)


user="attiq"
passw= "123"


def login(request,user_name, password):
  
      
   if user_name==user and password==passw:
      return render (request, "course/login.html")
  
   return render(request, "course/home.html")


def signup(request):
   return render(request, "course/signup.html")