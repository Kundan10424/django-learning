from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username'] = 'John'
    request.session['course'] = 'Django'
    return HttpResponse("Session data saved successfully")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f"Hello {username}, you are learning {course}")

def delete_session(request):
    # try:
    #     del request.session['username']
    #     del request.session['course']

    # except:
    #     pass

    request.session.flush() # this will delte all session data

    return HttpResponse("Session data deleted successfully")
