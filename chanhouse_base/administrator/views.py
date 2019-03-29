from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'administrator/index.html', {})

#  def index(request):
#      return HttpResponse("Hello, world.")
