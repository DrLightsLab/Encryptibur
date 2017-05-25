from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

import json

def login(request):
    if request.method == 'GET':
        return render_to_response('login.html', {}, RequestContext(request))
    if request.method == 'POST':
        print 'printing request', request
        response = create_user(request)
        return render_to_response('login.html', response, RequestContext(request))

def create_user(data):
    user = User.objects.create_user(data.get_username(), data.get_email(), data.get_password())
    return data

def validate_user(data):
    user = user(username=data.get_username(), password=data.get_password())
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
