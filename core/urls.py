from django.contrib import admin
from django.urls import path, include

from tasks.views import get_status, run_task, welcome

urlpatterns = [
    path("", welcome, name='welcome'),
    path("admin/", admin.site.urls),
    path("tasks/<task_id>/", get_status, name="get_status"),
    path("tasks/", run_task, name="run_task"),
    path('', include('django_prometheus.urls'))
]
