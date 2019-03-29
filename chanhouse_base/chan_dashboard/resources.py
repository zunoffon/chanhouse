from chanhouse_base.chan_dashboard.views import Category
from import_export import resources


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
