from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
import json

def login(request):
    return render_to_response('login.html', {'data' : data}, RequestContext(request))
