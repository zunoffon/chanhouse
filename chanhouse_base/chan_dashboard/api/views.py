from rest_framework import generics
from ..models import BookDate
from .serializers import BookDateSerializer

from django.template.response import TemplateResponse
from django.http.response import HttpResponse


def dashboard(request):
    html = TemplateResponse(request, 'dashboard.html')
    return HttpResponse(html.render())


class BookDateListView(generics.ListAPIView):
    serializer_class = BookDateSerializer
    queryset = BookDate.objects.all()


