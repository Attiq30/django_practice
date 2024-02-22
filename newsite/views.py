from django.shortcuts import HttpResponse


def my_view(request):
    return HttpResponse("my name is attiq ur rehman")

def second_view(request):
     a=12 
     b=13
     c=a*b
     return HttpResponse( f"the answer of c will be {c}")