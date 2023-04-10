from django.shortcuts import render
from MovieTriggerApp.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.db.models import F,Q,Value,ExpressionWrapper,DecimalField,Func,Aggregate,Count,Sum,Min,Max ,Avg
from django.db.models.functions import Concat
from django.db import transaction

# Create your views here.
def ViewPage(request):
    queryset = Movie.objects.all()
    list(queryset)
    return render(request,'MovieTriggerApp/index.html',{'name':'This is our Movie list  ','queryset':queryset})