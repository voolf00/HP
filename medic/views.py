# -*- coding: utf-8 -*-
from  django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib.auth.forms import UserCreationForm
from  medic.forms import User_form_datails, Patient_list_Form
from  medic.models import Profile, Who, PotientList
from django.core.exceptions import ObjectDoesNotExist
import datetime

from django.contrib.auth.models import User

from django.core import serializers

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


def logout(request):
    auth.logout(request)
    return redirect('/unity/article/get/2')


def register(request):
    if Profile.objects.get(id=request.user.id).is_who != Who.objects.get(id=1):
        args = {}
        args.update(csrf(request))

        if request.POST:
            new_user_form = UserCreationForm(request.POST)
            new_profile_form = User_form_datails(request.POST)
            if new_user_form.is_valid() and new_profile_form.is_valid():
                user_f = new_user_form.save(commit=False)

                new_user_form.save()
                profile_user_id = user_f.id
                try:
                    profile_f = new_profile_form.save(commit=False)
                    profile_f.user_id_doctor = request.user
                    profile_f.user_id = User.objects.get(id=profile_user_id)
                    new_profile_form.save()
                except:

                    delUser = User.objects.get(id=profile_user_id)
                    delUser.delete()
                    return HttpResponse('error add profile')
                return redirect('/unity/auth/patient/')


            else:
                return HttpResponse('no valid data')
        else:
            args['form'] = UserCreationForm()
            args['form_ditails'] = User_form_datails
            args['user'] = request.user.username
            return render_to_response('register.html', args)
    else:
        return redirect('/utip')


def patients(request):
    if Profile.objects.get(id=request.user.id).is_who != Who.objects.get(id=1):
        args = {}

        args['patients'] = Profile.objects.filter(is_who=1)

        return render_to_response('patients.html', args)


def patient(request, patient_id):
    if request.user.id == Profile.objects.get(id=patient_id).user_id or Profile.objects.get(
            id=request.user.id).is_who != Who.objects.get(id=1):
        args = {}
        args['patient'] = Profile.objects.get(id=patient_id)
        return render_to_response('patient.html', args)


def patientLists(request, patient_id):
    if request.user.id == Profile.objects.get(id=patient_id).user_id or Profile.objects.get(
            id=request.user.id).is_who != Who.objects.get(id=1):
        args = {}
        args['patient_lists'] = PotientList.objects.filter(patient_user_id=patient_id)
        return render_to_response('patient_lists.html', args)


def patientList(request, patient_id, list_id):
    if request.user.id == Profile.objects.get(id=patient_id).user_id or Profile.objects.get(
            id=request.user.id).is_who != Who.objects.get(id=1):
        args = {}
        args['list'] = PotientList.objects.get(id=list_id)

        return render_to_response('patient_list.html', args)


def AddList(request, patient_id):
    if Profile.objects.get(id=request.user.id).is_who != Who.objects.get(id=1):
        args = {}
        args.update(csrf(request))
        if request.POST:
            new_patient_list_form = Patient_list_Form(request.POST)
            if new_patient_list_form.is_valid():
                form = new_patient_list_form.save(commit=False)
                # add_user_profile =Profile.objects.get(user_id=request.user.id).id



                add_id_user = request.user.id

                form.add_user_id = Profile.objects.get(user_id_id=add_id_user)
                form.add_date = datetime.datetime.today()
                form.patient_user_id = Profile.objects.get(user_id=patient_id)
                new_patient_list_form.save()
                # return HttpResponse(form.id)
                return redirect("/unity/auth/patient/get/" + str(patient_id) + "/list/" + str(form.id))
            else:
                return HttpResponse('No valid')
        else:
            args['list_form'] = Patient_list_Form
            args['patient_id'] = patient_id
            return render_to_response('patientAddList.html', args)
    else:
        return HttpResponse('No glavdoctor')