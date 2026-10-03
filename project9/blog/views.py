from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_cookie(request):
    response = HttpResponse("Cookie set successfully")
    response.set_cookie('username','John Doe',max_age=60*60*24) #cookie will persist for one day
    response.set_cookie('course','Django', max_age=60*60*24)
    return response

def get_cookie(request):

    return HttpResponse("Cookie retreived Successfully")

def delete_cookie(request):

    return HttpResponse("Cookie Deleted Successfully")
