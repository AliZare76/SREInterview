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
    html = """<!DOCTYPE html>
                <html>
                <head>
                <!-- HTML Codes by Quackit.com -->
                <title>
                Welcome</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                body {background-color:#ffffff;background-repeat:no-repeat;background-position:top left;background-attachment:fixed;}
                h1{text-align:center;font-family:Arial, sans-serif;color:#000000;background-color:#ffffff;}
                p {text-align:center;font-family:Georgia, serif;font-size:18px;font-style:normal;font-weight:normal;color:#000000;background-color:#ffffff;}
                </style>
                </head>
                <body>
                <h1>SREInterview</h1>
                <p>to use the project : curl -F duration=60 https://sre.demoo.lol/tasks/ </p>
                <p>then : curl https:/sre.demoo.lol/tasks/task_id/</p>
                <p></p>
                <p></p>
                </body>
                </html>"""

    return HttpResponse(html, status=200)
