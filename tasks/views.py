from celery.result import AsyncResult
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from tasks.sample_tasks import create_task


@csrf_exempt
def run_task(request):
    if request.POST:
        duration = request.POST.get("duration")
        task = create_task.delay(int(duration))
        return JsonResponse({"task_id": task.id}, status=202)


@csrf_exempt
def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)


@csrf_exempt
def welcome(request):
    return HttpResponse('Welcome', status=200)
