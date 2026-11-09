from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health(request):
    return JsonResponse({"status": "ok", "app": "MindOS"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),
]