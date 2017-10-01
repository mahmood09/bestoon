# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from .models import User , Income , Expense , Token
from datetime import datetime
# Create your views here.


@csrf_exempt
def submit_expens (request):
    """ user submit requset """
#TODO: validates
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' in request.POST:
        date = request.POST['date'];
    else:
        date = datetime.now()
    Expense.objects.create(user = this_user , amount = request.POST['amount'],
                           text = request.POST['text'],date=date)
    print request.POST

    return JsonResponse({
        'status':'ok'
    },encoder=JSONEncoder)

@csrf_exempt
def submit_income (request):
    """ user submit requset """
#TODO: validates
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' in request.POST:
        date = request.POST['date'];
    else:
        date = datetime.now()
    Income.objects.create(user = this_user , amount = request.POST['amount'],
                           text = request.POST['text'],date=date)
    print request.POST

    return JsonResponse({
        'status':'ok'
    },encoder=JSONEncoder)