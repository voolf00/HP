from  django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse, StreamingHttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_protect
# Create your views here.


def login(request):
    args = {}

    args.update(csrf(request))

    args['test'] = 'test'

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/unity/article/get/2')
        else:
            args['errorr'] = "Fail User"
            return StreamingHttpResponse(args['error'])
    else:
        args['login'] = 'login'
        return render_to_response('login.html', args)


def logout(requset):
    auth.logout(requset)
    return redirect('/unity/article/get/2')