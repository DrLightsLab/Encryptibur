from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    foo = "moo"
    if request.method == 'GET':
        print "in GET request"
        #return render(request, "encryptibur/stone.html", {'foo' : foo})
        return render_to_response('encryptibur/stone.html',
        {'foo': foo},
        RequestContext(request))
        # return HttpResponse('Bar')
    else:
        return HttpResponse('Foo')
