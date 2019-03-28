from rest_framework import generics
from datetime import date
from ..models import BookDate
from .serializers import BookDateSerializer
# Create views for dashboard
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.template.response import TemplateResponse
from django.http.response import HttpResponse


def dashboard(request):
    html = TemplateResponse(request, 'dashboard.html')
    return HttpResponse(html.render())


class BookDateListView(generics.ListAPIView):
    serializer_class = BookDateSerializer
    today = date.today()

    def get_queryset(self):
        queryset_list = BookDate.objects.all()
        query = self.request.Get.get("s")
        if query:
            queryset_list = queryset_list.filter('user')
        return queryset_list

