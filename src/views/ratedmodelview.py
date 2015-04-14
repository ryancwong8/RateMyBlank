from django.shortcuts import render

from src.models.ratedmodel import RatedModel
from src.models.ratedobject import RatedObject
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.http import HttpResponseRedirect

def index(request):
  current_user = request.user
  ratedmodels = RatedModel.objects.order_by("-created_at")
  return render(request, 'index.html', {"ratedmodels": ratedmodels, "current_user": current_user})

def show(request, ratedModelName, ratedModelId):
  current_user = request.user
  ratedobjects = RatedObject.objects.filter(rated_model_id = ratedModelId).order_by("-created_at")
  ratedmodel = RatedModel.objects.get(pk=ratedModelId)
  return render(request, 'ratedmodel.html', {"ratedobjects": ratedobjects, "current_user": current_user, "ratedmodel": ratedmodel})

def submit(request):
  current_user = request.user
  return render(request, 'submit_ratedmodel.html', {"current_user": current_user})