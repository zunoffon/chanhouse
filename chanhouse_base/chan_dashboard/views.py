from django.shortcuts import render,get_object_or_404
from .models import User, Category, BookDate
from datetime import datetime, date


# Create your views here.
def bookDate_today(request):
    bookdated = BookDate.objects.all()
    return render(request, '../../chan_dashboard/templates/dashboard.html', {'bookdated': bookdated})
