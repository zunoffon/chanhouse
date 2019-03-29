from django.shortcuts import render,get_object_or_404
from .models import User, Category, BookDate
from .resources import CategoryResource
from import_export import resources
from tablib import Dataset

from django.http.response import HttpResponse
from django.template.response import TemplateResponse


# Create your views here.
def simple_upload(request):
    html = TemplateResponse(request, 'upload_category.html')
    if request.method == 'POST':
        category_resource = CategoryResource
        dataset = Dataset()
        new_categories = request.FILES['myfile']
        imported_data = dataset.load(new_categories.read())
        result = category_resource.import_data(imported_data, dry_run=True)

        if not result.has_errors():
            category_resource.import_data(imported_data, dry_run=False)

    return HttpResponse(html.render())


def bookDate_today(request):
    bookdated = BookDate.objects.all()
    return render(request, 'dashboard.html', {'bookdated': bookdated})
