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

#user_name =input("emter your name: ")
#password=input("enter your password: ")

def signup(request, user_name, password):
   if user_name=="attiq" and password=="123":
      return render(request, "course/signup.html")
   return render(request, "course/home.html")

.0 

def login_view(request):
    if request.method == 'POST':
       
        return redirect('dashboard')
    else:
        return render(request, 'course/login.html')
    


def dashboard_view(request):
    d={"name":"Attiq Ur Rehman",
       }
    
    return render(request, 'course/home.html', d)

