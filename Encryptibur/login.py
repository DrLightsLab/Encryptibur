from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import requires_csrf_token
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

import json

@requires_csrf_token
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        print 'printing request', request
        response = create_user(request)
        return render('login.html', response, RequestContext(request))

def create_user(data):
    user = User.objects.create_user(data.get_username(), data.get_email(), data.get_password())
    return data

def validate_user(data):
    print 'printing data', data
    #user = user(username=data.get_username(), password=data.get_password())
    if user is not None:
        if user.is_active:
            print('User is valid, active, and authenticated.')
        else:
            print('The password is valid, but the account has been disabled.')
    else:
        print('The username and the password were incoorect.')
    return user

#TODO: Complete method so that user can be updated.
def update_user(data):
    return data
