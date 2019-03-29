from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.bookDate_today),
    path('upload_file', views.simple_upload),
    path('api/', include('chanhouse_base.chan_dashboard.api.urls')),
]
